#!/usr/bin/env python3

import argparse
from datetime import date, timedelta
from pathlib import Path


TASKS_BY_MODE = {
    7: [
        "定义叙事主线与成功指标，输出最小可行场景图",
        "搭建 React + Vite 骨架并接入主题切换机制",
        "完成封面、痛点、方案三屏与基础导航",
        "完成证据、架构、CTA 三屏与进度指示",
        "补充核心转场、键盘导航与目录跳转",
        "做移动端适配与 reduced-motion 降级",
        "性能优化、发布素材整理与 Demo 复盘",
    ],
    14: [
        "定义叙事主线与成功指标",
        "输出逐屏信息架构与 Scene 清单",
        "搭建 React + Vite 项目骨架",
        "建立主题令牌与样式切换机制",
        "实现全局导航与进度指示",
        "完成封面、痛点、方案三屏",
        "完成证据、架构、CTA 三屏",
        "加入核心转场与分层入场动效",
        "补充键盘导航与目录跳转",
        "移动端适配与断点优化",
        "处理 reduced-motion 降级",
        "性能优化与资源压缩",
        "编写 README 与发布素材",
        "发布 Demo 并输出复盘",
    ],
}


def build_plan(project: str, audience: str, style: str, start_date: date, mode: int) -> str:
    tasks = TASKS_BY_MODE[mode]
    lines = [
        f"# {project} - {mode}天执行计划",
        "",
        f"- 目标受众：{audience}",
        f"- 主风格：{style}",
        f"- 执行模式：{mode}天",
        f"- 开始日期：{start_date.isoformat()}",
        "",
        "## 日计划",
        "",
    ]

    for idx, task in enumerate(tasks, start=1):
        day = start_date + timedelta(days=idx - 1)
        lines.append(f"### Day {idx} - {day.isoformat()}")
        lines.append(f"- 任务：{task}")
        lines.append("- 交付：当日可验证产物")
        lines.append("")

    lines.append("## 每周目标")
    lines.append("")

    if mode == 7:
        lines.extend(
            [
                "- Week 1：完成 MVP 场景、主题切换、基础动效、发布素材",
                "- 目标：7天内拿到首个可访问 Demo 与可迭代反馈",
            ]
        )
    else:
        lines.extend(
            [
                "- Week 1：完成结构、主题系统、核心场景",
                "- Week 2：完成动效、优化、发布与分发",
            ]
        )

    lines.extend(
        [
            "",
            "## KPI",
            "",
            "- Demo 可访问且移动端可用",
            "- Lighthouse Performance >= 85",
            "- Lighthouse Accessibility >= 90",
        ]
    )

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a 7/14-day showcase build plan")
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument("--audience", required=True, help="Target audience")
    parser.add_argument("--style", default="neo-luxury", help="Primary visual style")
    parser.add_argument("--mode", type=int, choices=[7, 14], default=14, help="Execution mode (7 or 14 days)")
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
    content = build_plan(args.project, args.audience, args.style, start, args.mode)
    output.write_text(content, encoding="utf-8")
    print(f"Plan written to {output}")


if __name__ == "__main__":
    main()
