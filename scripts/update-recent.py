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


def sh(*args):
    return subprocess.check_output(args, cwd=ROOT).decode("utf-8", "ignore")


def platform_from_parts(parts):
    top = parts[0]
    if top in TARGET_DIRS:
        return TARGET_DIRS[top]
    if LEETCODE_SLUG.fullmatch(top):
        return "LeetCode"
    return None


def title_from_rel_dir(rel_dir):
    return pathlib.Path(rel_dir).name.replace(" ", " ").strip()


def encode_rel_path(rel_dir):
    return "/".join(quote(part) for part in pathlib.Path(rel_dir).parts)


def recent_changed_dirs(limit=LIMIT):
    try:
        log = sh("git", "log", "--name-only", f"--pretty=format:{COMMIT_PREFIX}%cd", "--date=short")
    except Exception:
        return fallback_recent_dirs(limit)

    seen = set()
    rows = []
    date = ""

    for line in log.splitlines():
        if not line:
            continue
        if line.startswith(COMMIT_PREFIX):
            date = line[len(COMMIT_PREFIX) :].strip()
            continue
        if not date:
            continue

        parts = pathlib.Path(line).parts
        if not parts:
            continue

        platform = platform_from_parts(parts)
        if not platform:
            continue

        file_path = ROOT / line
        if not file_path.exists() or file_path.suffix not in EXTS:
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
