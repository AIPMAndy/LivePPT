#!/usr/bin/env python3

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path


DEFAULT_SUBTITLE = "Turn your README into a clickable HTML deck without rebuilding your project as a frontend app."


def clean_markdown(text: str) -> str:
    lines = text.splitlines()
    cleaned = []
    in_html_block = False
    seen_h1 = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("<div"):
            in_html_block = True
            continue
        if in_html_block:
            if stripped.endswith("</div>") or stripped == "</div>":
                in_html_block = False
            continue

        if stripped.startswith("![") and "](assets/" in stripped:
            continue
        if stripped.startswith("[") and "](" in stripped and "|" in stripped and not seen_h1:
            continue
        if stripped.startswith("[!["):
            continue
        if stripped in {"---", "***"}:
            continue

        if stripped.startswith("# "):
            seen_h1 = True
            cleaned.append(line)
            continue

        if stripped.startswith("## "):
            # Collapse overly meta sections into user-facing names.
            title = stripped[3:].strip()
            rename_map = {
                "What LivePPT Is": "What This Project Does",
                "LivePPT 是什么": "这个项目能做什么",
                "Why the Main Entry Should Not Be a “14-Day Plan”": "Why HTML Output Comes First",
                "为什么不是先生成“14 天执行计划”": "为什么先出 HTML",
                "30-Second Quick Start": "Quick Start",
                "30 秒快速开始": "快速开始",
                "Current Core Capabilities": "Core Capabilities",
                "当前核心能力": "核心能力",
                "Current Boundaries": "Current Boundaries",
                "当前边界": "当前边界",
                "Common Commands": "Common Commands",
                "常用命令": "常用命令",
            }
            cleaned.append(f"## {rename_map.get(title, title)}")
            continue

        # strip excessive badge-heavy / command-heavy noise from first screen
        if not seen_h1 and stripped.startswith((">", "- ", "* ")):
            continue

        # compress fenced code markers into simple bullets so deck pages stay readable
        if stripped.startswith("```"):
            continue

        if stripped:
            stripped = re.sub(r"`([^`]+)`", r"\1", stripped)

        cleaned.append(stripped)

    result = "\n".join(cleaned)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip() + "\n"


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a README.md into a standalone HTML deck")
    parser.add_argument("input", help="Input README markdown path")
    parser.add_argument("--output", required=True, help="Output HTML path")
    parser.add_argument("--theme", default="neo-luxury", help="Visual theme preset")
    parser.add_argument("--brand", default="LivePPT", help="Brand text shown in deck")
    parser.add_argument("--subtitle", default=DEFAULT_SUBTITLE, help="Cover subtitle")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    input_path = Path(args.input)
    cleaned = clean_markdown(input_path.read_text(encoding="utf-8"))

    with tempfile.TemporaryDirectory(prefix="liveppt-readme-") as temp_dir:
        temp_path = Path(temp_dir) / "cleaned-readme.md"
        temp_path.write_text(cleaned, encoding="utf-8")
        render_cmd = [
            sys.executable,
            "scripts/render_plan_to_html.py",
            str(temp_path),
            "--output",
            args.output,
            "--theme",
            args.theme,
            "--brand",
            args.brand,
            "--subtitle",
            args.subtitle,
        ]
        run(render_cmd, root)

    print(f"README deck written to {args.output}")


if __name__ == "__main__":
    main()
