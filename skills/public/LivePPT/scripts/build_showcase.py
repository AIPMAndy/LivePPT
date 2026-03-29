#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path


PRESET_SUBTITLES = {
    "neo-luxury": "用更稳、更高级、更有发布会感的方式讲清楚你的项目价值。",
    "cyber-pulse": "让你的项目像一次 AI 新品发布，节奏更快，记忆点更强。",
    "minimal-editorial": "把复杂内容整理成更清晰、更耐读的网页演示。",
    "brutalist-bold": "用更直接、更有冲击力的方式传达你的核心主张。",
    "prism-command": "把你的方案讲得更像一套可执行的企业级系统。",
    "linen-editorial": "把策略、叙事和审美统一成一份更稳的展示页面。",
    "signal-night": "适合技术、平台、基础设施类能力展示的演示风格。",
}


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a showcase markdown plan and render it to a standalone HTML deck"
    )
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument("--audience", required=True, help="Target audience")
    parser.add_argument("--style", default="neo-luxury", help="Primary visual style preset")
    parser.add_argument("--plan-output", default="plans/generated-plan.md", help="Output markdown plan path")
    parser.add_argument("--html-output", default="dist/index.html", help="Output html path")
    parser.add_argument("--brand", default="LivePPT", help="Brand text displayed in the cover and footer")
    parser.add_argument("--subtitle", help="Custom subtitle for cover page")
    parser.add_argument("--start-date", help="Plan start date in YYYY-MM-DD")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    plan_output = Path(args.plan_output)
    html_output = Path(args.html_output)
    subtitle = args.subtitle or PRESET_SUBTITLES.get(args.style, PRESET_SUBTITLES["neo-luxury"])

    generate_cmd = [
        sys.executable,
        "scripts/generate_showcase_plan.py",
        "--project",
        args.project,
        "--audience",
        args.audience,
        "--style",
        args.style,
        "--output",
        str(plan_output),
    ]
    if args.start_date:
        generate_cmd.extend(["--start-date", args.start_date])

    render_cmd = [
        sys.executable,
        "scripts/render_plan_to_html.py",
        str(plan_output),
        "--output",
        str(html_output),
        "--brand",
        args.brand,
        "--theme",
        args.style,
        "--subtitle",
        subtitle,
    ]

    run(generate_cmd, root)
    run(render_cmd, root)

    print(f"Plan written to {plan_output}")
    print(f"HTML deck written to {html_output}")


if __name__ == "__main__":
    main()
