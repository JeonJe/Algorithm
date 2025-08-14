#!/usr/bin/env python3
import subprocess, re, pathlib, itertools

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
TARGET_DIRS = ["LeetCode", "Programmers", "Baekjoon"]
EXTS = {".java", ".py", ".kt", ".js", ".ts", ".cpp", ".c"}
LIMIT = 10

def sh(*args):
    return subprocess.check_output(args, cwd=ROOT).decode("utf-8", "ignore")

def recent_changed_files(limit=LIMIT):
    log = sh("git", "log", "--name-only", "--pretty=format:%H|%cd", "--date=short", "--", *TARGET_DIRS)
    seen = set()
    items = []
    for block in log.split("\n\n"):
        if "|" not in block: 
            continue
        header, *files = block.splitlines()
        _, date = header.split("|", 1)
        for f in files:
            if not f or f.startswith(" "): 
                continue
            p = (ROOT / f)
            if not p.exists(): 
                continue
            if p.suffix not in EXTS: 
                continue
            # 최상위 폴더로 플랫폼 판별
            parts = pathlib.Path(f).parts
            if not parts: 
                continue
            top = parts[0]
            if top not in TARGET_DIRS: 
                continue
            rel = "/".join(parts)
            if rel in seen: 
                continue
            seen.add(rel)
            items.append((date, rel, top))
            if len(items) >= limit:
                return items
    return items

def read_title(path: pathlib.Path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            for _ in range(5):
                line = fp.readline()
                if not line: break
                m = re.search(r"(?:Problem|문제)\s*:\s*(.+)", line, re.I)
                if m:
                    return m.group(1).strip()
    except Exception:
        pass
    # 없으면 파일명에서 추정
    name = path.stem
    return name

def platform_of(top_folder: str):
    return {"LeetCode":"LeetCode", "Programmers":"Programmers", "Baekjoon":"Baekjoon"}.get(top_folder, top_folder)

def build_table(rows):
    if not rows:
        return "_최근 변경된 풀이가 없어요._"
    lines = ["| 날짜 | 문제 | 플랫폼 | 링크 |",
             "|---|---|---|---|"]
    for date, rel, top in rows:
        title = read_title(ROOT / rel)
        plat = platform_of(top)
        url = f"./{rel}"
        lines.append(f"| {date} | **{title}** | {plat} | [코드]({url}) |")
    return "\n".join(lines)

def replace_between(text, start_tag, end_tag, replacement):
    import re
    pattern = re.compile(f"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.S)
    return pattern.sub(f"{start_tag}\n{replacement}\n{end_tag}", text)

def main():
    rows = recent_changed_files()
    md = build_table(rows)
    start_tag = "<!-- RECENT_SOLUTIONS:START -->"
    end_tag = "<!-- RECENT_SOLUTIONS:END -->"
    readme = README.read_text(encoding="utf-8")
    updated = replace_between(readme, start_tag, end_tag, md)
    if updated != readme:
        README.write_text(updated, encoding="utf-8")
        print("README updated.")
    else:
        print("No changes.")

if __name__ == "__main__":
    main()
