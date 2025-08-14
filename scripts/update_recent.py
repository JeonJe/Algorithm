#!/usr/bin/env python3
import os, subprocess, re, pathlib
from typing import List, Tuple

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
LIMIT = int(os.environ.get("LIMIT", "20"))

# 제외할 경로/파일 패턴
EXCLUDE_DIRS = {".git", ".github", "scripts", "docs", "node_modules", "build", "out", "dist", "__pycache__"}
EXCLUDE_FILES = {"README.md", "README.MD", "readme.md"}
EXCLUDE_EXTS = {".md", ".yml", ".yaml", ".json", ".lock", ".txt"}
# 허용 언어 확장자
INCLUDE_EXTS = {".java", ".kt", ".py", ".js", ".ts", ".cpp", ".c", ".go", ".rs"}

START_TAG = "<!-- RECENT_SOLUTIONS:START -->"
END_TAG   = "<!-- RECENT_SOLUTIONS:END -->"

def sh(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT).decode("utf-8", "ignore")

def is_excluded(rel: str) -> bool:
    p = pathlib.Path(rel)
    # 디렉토리 제외
    for part in p.parts:
        if part in EXCLUDE_DIRS:
            return True
    # 파일명 제외
    if p.name in EXCLUDE_FILES:
        return True
    # 확장자 제외
    if p.suffix in EXCLUDE_EXTS:
        return True
    return False

def is_included(rel: str) -> bool:
    return pathlib.Path(rel).suffix in INCLUDE_EXTS and not is_excluded(rel)

def recent_changed_files(limit: int) -> List[Tuple[str,str]]:
    """
    returns list of (date, relative_path) by most recent commit that touched each file.
    """
    # --name-only 으로 전체 파일 히스토리를 시간 역순으로 쭉 받고, 한 파일당 가장 최신 등장만 채택
    log = sh("git", "log", "--name-only", "--pretty=format:%H|%cd", "--date=short", "--", ".")
    seen = set()
    items: List[Tuple[str,str]] = []
    for block in log.split("\n\n"):
        lines = [ln for ln in block.splitlines() if ln.strip()]
        if not lines or "|" not in lines[0]:
            continue
        header = lines[0]
        _, date = header.split("|", 1)
        for f in lines[1:]:
            rel = f.strip()
            if not rel or rel.endswith("/"):
                continue
            if rel in seen:
                continue
            if not is_included(rel):
                continue
            # 실제 파일 존재하는 최신 스냅샷만
            if not (ROOT / rel).exists():
                continue
            seen.add(rel)
            items.append((date, rel))
            if len(items) >= limit:
                return items
    return items

def read_problem_title(path: pathlib.Path) -> str:
    """
    파일 첫 5줄에서 'Problem:' 또는 '문제:' 주석 패턴을 찾으면 제목 사용, 없으면 파일명.
    """
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            for _ in range(5):
                line = fp.readline()
                if not line:
                    break
                m = re.search(r"(?:Problem|문제)\s*:\s*(.+)", line, re.I)
                if m:
                    return m.group(1).strip()
    except Exception:
        pass
    return path.stem

def platform_guess(rel: str) -> str:
    # 상위 폴더명으로 대략 추정(없으면 빈칸)
    parts = pathlib.Path(rel).parts
    return parts[0] if parts else ""

def build_table(rows: List[Tuple[str,str]]) -> str:
    if not rows:
        return "_최근 변경된 풀이 파일을 찾지 못했습니다._"
    lines = [
        "| 날짜 | 문제 | 위치 | 링크 |",
        "|---|---|---|---|",
    ]
    for date, rel in rows:
        title = read_problem_title(ROOT / rel)
        plat = platform_guess(rel)
        url = f"./{rel}"
        display_loc = plat if plat else "-"
        lines.append(f"| {date} | **{title}** | {display_loc} | [코드]({url}) |")
    return "\n".join(lines)

def replace_between(text: str, start_tag: str, end_tag: str, replacement: str) -> str:
    import re
    pattern = re.compile(f"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.S)
    return pattern.sub(f"{start_tag}\n{replacement}\n{end_tag}", text)

def main():
    rows = recent_changed_files(LIMIT)
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
