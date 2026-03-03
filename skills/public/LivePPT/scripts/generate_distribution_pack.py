#!/usr/bin/env python3

import argparse
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


def build_schedule(release_date: date) -> list[tuple[str, str, str]]:
    shanghai = ZoneInfo("Asia/Shanghai")
    eastern = ZoneInfo("America/New_York")

    checkpoints = [
        ("Wave 1", datetime(release_date.year, release_date.month, release_date.day, 10, 30, tzinfo=shanghai), "X + 微信朋友圈"),
        ("Wave 2", datetime(release_date.year, release_date.month, release_date.day, 22, 0, tzinfo=shanghai), "Show HN + Reddit"),
        ("Wave 3", datetime(release_date.year, release_date.month, release_date.day, 22, 45, tzinfo=shanghai), "V2EX + 掘金"),
        ("Wave 4", datetime(release_date.year, release_date.month, release_date.day, 23, 30, tzinfo=shanghai), "知乎回答/文章"),
        ("Wave 5", datetime(release_date.year, release_date.month, release_date.day, 10, 0, tzinfo=shanghai) + timedelta(days=1), "复盘数据 + 二次转发"),
    ]

    rows = []
    for wave, slot, channel in checkpoints:
        cn_time = slot.strftime("%Y-%m-%d %H:%M")
        us_time = slot.astimezone(eastern).strftime("%Y-%m-%d %H:%M")
        rows.append((wave, f"{cn_time} (UTC+8) / {us_time} (ET)", channel))
    return rows


def build_markdown(project: str, repo: str, demo: str, version: str, release_date: date) -> str:
    schedule_rows = "\n".join(
        f"| {wave} | {when} | {channel} |" for wave, when, channel in build_schedule(release_date)
    )

    return "\n".join(
        [
            f"# {project} 分发文案包（{version}）",
            "",
            f"- 发布日期：{release_date.isoformat()}",
            f"- GitHub：{repo}",
            f"- Demo：{demo}",
            "",
            "## 一句话定位",
            "",
            "- 中文：把 README 变成可点击、可换风格、可发布的动态网页演示。",
            "- English: Turn README into a clickable, theme-switchable, launch-ready web showcase.",
            "",
            "## X / Twitter（中文）",
            "",
            "```text",
            f"刚把 {project} 做成了开源可复用版本：{version}",
            "",
            "它解决的不是“怎么写文档”，而是“怎么让项目被看懂、被记住、被转发”。",
            "",
            "你可以得到：",
            "• 可点击分镜演示",
            "• 多主题运行时切换",
            "• 从计划到发布的脚本化流程",
            "",
            f"GitHub: {repo}",
            f"Demo: {demo}",
            "",
            "#OpenSource #WebDesign #DeveloperTools #Presentation",
            "```",
            "",
            "## X / Twitter（English）",
            "",
            "```text",
            f"Just shipped {project} {version}.",
            "",
            "It helps you turn a plain README into a clickable launch-style web showcase.",
            "",
            "What you get:",
            "- Scene-based storytelling",
            "- Runtime theme switching",
            "- Scripted workflow from plan to release",
            "",
            f"GitHub: {repo}",
            f"Demo: {demo}",
            "",
            "#opensource #webdev #devtools #showcase",
            "```",
            "",
            "## Hacker News（Show HN）",
            "",
            "- Title: `Show HN: LivePPT – Turn README into a clickable launch web showcase`",
            "- First comment:",
            "",
            "```text",
            "I built LivePPT to solve a recurring launch problem:",
            "great repos often have strong code but weak storytelling.",
            "",
            "LivePPT converts linear project docs into scene-based, click-through web decks.",
            "It includes runtime theme switching, keyboard navigation, and release workflow scripts.",
            "",
            "I would love feedback on:",
            "1) clarity of the scene flow,",
            "2) theme presets for B2B launches,",
            "3) what blocks adoption in your current release workflow.",
            "```",
            "",
            "## Reddit（r/SideProject 或 r/webdev）",
            "",
            "```text",
            "I open-sourced LivePPT, a tool to transform README-style project intros into clickable launch decks.",
            "",
            "Main idea:",
            "- keep one narrative spine",
            "- switch visual themes without rewriting content",
            "- ship with scripts + docs for repeatable releases",
            "",
            f"Repo: {repo}",
            f"Demo: {demo}",
            "",
            "I am looking for blunt feedback on what would make this genuinely useful in your workflow.",
            "```",
            "",
            "## 中文社区短帖（V2EX / 掘金 / 知乎）",
            "",
            "```text",
            "开源了一个我自己在用的项目发布工作流：LivePPT。",
            "",
            "核心不是做“更花哨的 PPT”，而是把 README 的信息密度变成“可讲述”的分镜体验：",
            "1) 点击切屏 + 键盘控制",
            "2) 同一内容多主题切换",
            "3) 从计划、主题、校验到 release note 的脚本化闭环",
            "",
            f"仓库：{repo}",
            f"演示：{demo}",
            "",
            "欢迎直接拍砖：你觉得它最该补的第一能力是什么？",
            "```",
            "",
            "## 72 小时节奏",
            "",
            "| 波次 | 时间 | 动作 |",
            "|------|------|------|",
            schedule_rows,
            "",
            "## 复盘指标",
            "",
            "- 24h：GitHub 访问 -> Star 转化率",
            "- 48h：Demo 访问 -> Star/Fork 转化率",
            "- 72h：Issue/Discussion 数量 + 关键词聚类（真实需求）",
            "",
            "## 快速执行清单",
            "",
            "- [ ] 发布前再次执行 `make validate`",
            "- [ ] README 首屏保持和 Demo 视觉一致",
            "- [ ] 每个平台首条评论加“你最想要的能力”提问",
            "- [ ] 72 小时内至少回复 90% 反馈",
            "",
        ]
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a multi-channel distribution copy pack")
    parser.add_argument("--project", default="LivePPT", help="Project name")
    parser.add_argument("--repo", default="https://github.com/AIPMAndy/LivePPT", help="GitHub repository URL")
    parser.add_argument("--demo", default="http://localhost:4188", help="Demo URL")
    parser.add_argument("--version", default="v0.1.2", help="Release version")
    parser.add_argument("--date", default=date.today().isoformat(), help="Release date YYYY-MM-DD")
    parser.add_argument("--output", help="Output markdown path (default: releases/distribution-pack-<date>.md)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    release_date = date.fromisoformat(args.date)
    root = Path(__file__).resolve().parents[1]
    output = Path(args.output) if args.output else root / "releases" / f"distribution-pack-{release_date.isoformat()}.md"
    output.parent.mkdir(parents=True, exist_ok=True)

    content = build_markdown(args.project, args.repo, args.demo, args.version, release_date)
    output.write_text(content, encoding="utf-8")
    print(f"Distribution pack written to {output}")


if __name__ == "__main__":
    main()
