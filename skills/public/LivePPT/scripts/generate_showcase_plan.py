#!/usr/bin/env python3

import argparse
from datetime import date
from pathlib import Path


PHASES = [
    ("叙事定义", "定义叙事主线与成功指标", "最小可行场景图与核心指标说明"),
    ("信息架构", "输出逐屏信息架构与 Scene 清单", "可评审的场景地图与内容草图"),
    ("工程搭建", "搭建 React + Vite 骨架并接入主题切换机制", "可运行的基础工程与主题切换能力"),
    ("核心场景", "完成封面、痛点、方案、证据、架构、CTA 六屏", "可点击演示的核心路径"),
    ("交互完善", "补充转场、键盘导航、目录跳转与进度指示", "完整交互闭环与可访问性降级"),
    ("发布准备", "完成性能优化、移动端适配与发布素材整理", "可发布 Demo 与复盘要点"),
]


def build_plan(project: str, audience: str, style: str, start_date: date) -> str:
    lines = [
        f"# {project} - 阶段执行清单",
        "",
        f"- 目标受众：{audience}",
        f"- 主风格：{style}",
        f"- 开始日期：{start_date.isoformat()}",
        "",
        "## 阶段清单",
        "",
    ]

    for idx, (phase, task, deliverable) in enumerate(PHASES, start=1):
        lines.append(f"### 阶段 {idx}：{phase}")
        lines.append(f"- 任务：{task}")
        lines.append(f"- 交付：{deliverable}")
        lines.append("")

    lines.extend(
        [
            "## KPI",
            "",
            "- Demo 可访问且移动端可用",
            "- Lighthouse Performance >= 85",
            "- Lighthouse Accessibility >= 90",
        ]
    )

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a showcase implementation checklist")
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument("--audience", required=True, help="Target audience")
    parser.add_argument("--style", default="neo-luxury", help="Primary visual style")
    parser.add_argument("--output", required=True, help="Output markdown path")
    parser.add_argument(
        "--start-date",
        default=date.today().isoformat(),
        help="Plan start date in YYYY-MM-DD",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    start = date.fromisoformat(args.start_date)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    content = build_plan(args.project, args.audience, args.style, start)
    output.write_text(content, encoding="utf-8")
    print(f"Checklist written to {output}")


if __name__ == "__main__":
    main()
