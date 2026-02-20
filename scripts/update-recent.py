#!/usr/bin/env python3
import os
import pathlib
import re
import subprocess
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
LIMIT = int(os.environ.get("LIMIT", "20"))

TARGET_DIRS = {
    "LeetCode": "LeetCode",
    "프로그래머스": "Programmers",
    "백준": "Baekjoon",
    "CodeTree": "CodeTree",
    "코드트리": "CodeTree",
}
EXTS = {".java", ".py", ".kt", ".js", ".ts", ".cpp", ".c", ".sql", ".go", ".rs"}

START_TAG = "<!-- RECENT_SOLUTIONS:START -->"
END_TAG = "<!-- RECENT_SOLUTIONS:END -->"
COMMIT_PREFIX = "__COMMIT__"
LEETCODE_SLUG = re.compile(r"^\d{4}-[a-z0-9-]+$")
DATE_DIR_SLUG = re.compile(r"^\d{6}$")
IGNORE_SUBJECT_PATTERNS = (
    re.compile(r"^chore:\s*reorganize solution folders", re.I),
    re.compile(r"^chore\(readme\):\s*refresh recent solutions list", re.I),
    re.compile(r"^chore\(readme\):\s*auto-update recent solutions", re.I),
)


def sh(*args):
    return subprocess.check_output(args, cwd=ROOT).decode("utf-8", "ignore")


def platform_from_parts(parts):
    top = parts[0]
    if top in TARGET_DIRS:
        return TARGET_DIRS[top]
    if LEETCODE_SLUG.fullmatch(top):
        return "LeetCode"
    return None


def should_ignore_subject(subject):
    return any(pattern.search(subject) for pattern in IGNORE_SUBJECT_PATTERNS)


def resolve_current_file_path(rel_path):
    path = pathlib.Path(rel_path)
    current = ROOT / path
    if current.exists():
        return path

    parts = path.parts
    if not parts:
        return None

    top = parts[0]

    # LeetHub 구형 구조: 0001-xxx/... -> LeetCode/0001-xxx/...
    if LEETCODE_SLUG.fullmatch(top):
        mapped = pathlib.Path("LeetCode") / path
        if (ROOT / mapped).exists():
            return mapped

    # CodeTree 날짜 구조: 250101/... -> CodeTree/250101/...
    if DATE_DIR_SLUG.fullmatch(top):
        mapped = pathlib.Path("CodeTree") / path
        if (ROOT / mapped).exists():
            return mapped

    # Java/백준/... -> 백준/...
    if len(parts) >= 3 and parts[0] == "Java" and parts[1] in {"백준", "Baekjoon"}:
        mapped = pathlib.Path("백준").joinpath(*parts[2:])
        if (ROOT / mapped).exists():
            return mapped

    return None


def title_from_rel_dir(rel_dir):
    return pathlib.Path(rel_dir).name.replace(" ", " ").strip()


def encode_rel_path(rel_dir):
    return "/".join(quote(part) for part in pathlib.Path(rel_dir).parts)


def recent_changed_dirs(limit=LIMIT):
    try:
        log = sh(
            "git",
            "log",
            "--name-only",
            f"--pretty=format:{COMMIT_PREFIX}%cd|%s",
            "--date=short",
        )
    except Exception:
        return fallback_recent_dirs(limit)

    seen = set()
    rows = []
    date = ""
    ignore_commit = False

    for line in log.splitlines():
        if not line:
            continue
        if line.startswith(COMMIT_PREFIX):
            payload = line[len(COMMIT_PREFIX) :].strip()
            if "|" in payload:
                date, subject = payload.split("|", 1)
            else:
                date, subject = payload, ""
            date = date.strip()
            ignore_commit = should_ignore_subject(subject.strip())
            continue
        if not date or ignore_commit:
            continue

        resolved = resolve_current_file_path(line)
        if not resolved:
            continue

        platform = platform_from_parts(resolved.parts)
        if not platform:
            continue

        file_path = ROOT / resolved
        if file_path.suffix not in EXTS:
            continue

        rel_dir = file_path.parent.relative_to(ROOT).as_posix()
        if rel_dir in seen:
            continue

        seen.add(rel_dir)
        rows.append((date, rel_dir, platform))
        if len(rows) >= limit:
            break
    return rows


def fallback_recent_dirs(limit=LIMIT):
    by_dir = {}
    for top, platform in TARGET_DIRS.items():
        base = ROOT / top
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.suffix not in EXTS:
                continue
            rel_dir = path.parent.relative_to(ROOT).as_posix()
            mtime = path.stat().st_mtime
            if rel_dir not in by_dir or mtime > by_dir[rel_dir][0]:
                by_dir[rel_dir] = (mtime, platform)

    sorted_rows = sorted(by_dir.items(), key=lambda item: item[1][0], reverse=True)
    rows = []
    for rel_dir, (_, platform) in sorted_rows[:limit]:
        rows.append(("N/A", rel_dir, platform))
    return rows


def build_table(rows):
    if not rows:
        return "_최근 변경된 풀이가 없어요._"

    lines = [
        "| 날짜 | 문제 | 플랫폼 | 링크 |",
        "|---|---|---|---|",
    ]
    for date, rel_dir, platform in rows:
        title = title_from_rel_dir(rel_dir).replace("|", r"\|")
        url = encode_rel_path(rel_dir)
        lines.append(f"| {date} | **{title}** | {platform} | [코드](./{url}) |")
    return "\n".join(lines)


def replace_between(text, start_tag, end_tag, replacement):
    pattern = re.compile(f"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.S)
    if not pattern.search(text):
        raise RuntimeError("README.md에 RECENT_SOLUTIONS 태그가 없습니다.")
    return pattern.sub(f"{start_tag}\n{replacement}\n{end_tag}", text)


def main():
    rows = recent_changed_dirs()
    md = build_table(rows)

    readme = README.read_text(encoding="utf-8")
    updated = replace_between(readme, START_TAG, END_TAG, md)
    if updated != readme:
        README.write_text(updated, encoding="utf-8")
        print("README updated.")
    else:
        print("No changes.")


if __name__ == "__main__":
    main()
