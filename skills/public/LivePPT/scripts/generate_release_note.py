#!/usr/bin/env python3

import argparse
from datetime import date
from pathlib import Path


def build_release_note(version: str, release_date: str, summary: str) -> str:
    lines = [
        f"# Release {version} - {release_date}",
        "",
        summary,
        "",
        "## ✨ Added",
        "",
        "- ",
        "",
        "## 🔄 Changed",
        "",
        "- ",
        "",
        "## 🐛 Fixed",
        "",
        "- ",
        "",
        "## ✅ Validation",
        "",
        "- `make validate` 通过",
        "",
        "## 🎯 User Value",
        "",
        "- ",
    ]
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate release note template")
    parser.add_argument("--version", required=True, help="Release version, e.g. v0.1.2")
    parser.add_argument("--summary", default="本版本聚焦稳定性和交付效率优化。", help="Release summary")
    parser.add_argument("--date", default=date.today().isoformat(), help="Release date in YYYY-MM-DD")
    parser.add_argument("--output", help="Output markdown path (default: releases/<version>.md)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    output = Path(args.output) if args.output else root / "releases" / f"{args.version}.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    content = build_release_note(args.version, args.date, args.summary)
    output.write_text(content, encoding="utf-8")
    print(f"Release note template written to {output}")


if __name__ == "__main__":
    main()
