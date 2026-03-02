<div align="center">

# 🚀 LivePPT

**把传统 PPT 升级为可点击切换的动态网页演示**  
**Turn static slides into cinematic, clickable web showcases**

[![Stars](https://img.shields.io/github/stars/AIPMAndy/LivePPT?style=social)](https://github.com/AIPMAndy/LivePPT/stargazers)
[![Forks](https://img.shields.io/github/forks/AIPMAndy/LivePPT?style=social)](https://github.com/AIPMAndy/LivePPT/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/AIPMAndy/LivePPT)](https://github.com/AIPMAndy/LivePPT/commits/main)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./skills/public/dynamic-showcase-web-skill/LICENSE)

**简体中文** | [English](#english)

</div>

---

> ⭐ 如果你也想做“高级感网页演示”，欢迎点个 Star 支持持续更新。

## 🎯 LivePPT 能帮你什么？

| 常见痛点 | LivePPT 解决方式 |
|---|---|
| PPT 只能线性播放，缺少互动感 | 场景化网页演示，支持点击、键盘、目录跳转 |
| 同一内容很难快速换风格 | 用主题令牌切换视觉，不改文案和结构 |
| 从想法到 Demo 周期太长 | 内置 7/14 天执行计划生成脚本 |
| 开源协作容易流程混乱 | `make validate` + CI + 发布模板统一节奏 |

## ✨ 核心能力

- **动态叙事工作流**：封面 → 痛点 → 方案 → 证据 → 架构 → CTA。
- **多风格主题系统**：`neo-luxury`、`cyber-pulse`、`minimal-editorial` 等。
- **自动化交付脚本**：计划生成、主题生成、发布说明生成。
- **开源协作标准化**：Contributing、Roadmap、Changelog、Launch Checklist。

## ⚡ 60 秒快速开始

```bash
cd skills/public/dynamic-showcase-web-skill

# 1) 校验结构与脚本
make validate

# 2) 生成 7 天执行计划
python3 scripts/generate_showcase_plan.py \
  --project "AI 产品发布网页演示" \
  --audience "技术决策者" \
  --mode 7 \
  --style "neo-luxury" \
  --output plans/7-day-plan.md

# 3) 生成一个新主题
python3 scripts/add_theme.py \
  --name "midnight-luxe" \
  --bg "#09090b" \
  --surface "#15151a" \
  --text "#f4f4f5" \
  --accent "#d4af37" \
  --motion "cubic-bezier(0.22, 1, 0.36, 1)" \
  --output themes/midnight-luxe.css
```

## 📁 仓库结构

```text
LivePPT/
├── README.md
└── skills/public/dynamic-showcase-web-skill/
    ├── SKILL.md
    ├── README.md
    ├── CHANGELOG.md
    ├── ROADMAP.md
    ├── OPEN_SOURCE_LAUNCH_CHECKLIST.md
    ├── scripts/
    ├── references/
    ├── assets/templates/
    └── releases/
```

## 🗺️ Roadmap

- [x] `v0.1.x`：技能工作流、脚本工具链、校验体系、发布文档。
- [ ] `v0.2.0`：Starter 前端模板、动效预设、Lighthouse 质量门禁。
- [ ] `v0.3.0`：社区主题生态、示例库与贡献者扩展。

## 🤝 贡献方式

- 提交新主题预设（颜色 / 字体 / 动效）。
- 提交新场景模板（路演 / 课程 / 发布会）。
- 提交脚本增强（自动校验、发布、文档生成）。

查看：`skills/public/dynamic-showcase-web-skill/CONTRIBUTING.md`

## 📄 License

MIT

---

## English

> Build premium, click-through web presentations instead of static slides.

### What LivePPT Does

- Converts linear slide requests into interactive scene-based web showcases.
- Supports runtime style switching via theme tokens.
- Provides 7/14-day execution plan generation for fast shipping.
- Includes validation + release scaffolding for open-source collaboration.

### Quick Start

```bash
cd skills/public/dynamic-showcase-web-skill
make validate
```

### Key Documents

- Skill spec: `skills/public/dynamic-showcase-web-skill/SKILL.md`
- Guide: `skills/public/dynamic-showcase-web-skill/README.md`
- Changelog: `skills/public/dynamic-showcase-web-skill/CHANGELOG.md`
- Launch checklist: `skills/public/dynamic-showcase-web-skill/OPEN_SOURCE_LAUNCH_CHECKLIST.md`

### Call for Contributors

If you are building high-end interactive demos for product launch, sales, education, or storytelling, feel free to open an Issue/PR and co-build LivePPT.
