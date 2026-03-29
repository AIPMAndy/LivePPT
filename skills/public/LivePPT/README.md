[English](README_EN.md) | **简体中文**

<div align="center">

# LivePPT

**把 Markdown / README 变成可点击、可翻页、可分享的 HTML 演示页。**

[![License](https://img.shields.io/badge/License-MIT%20%2B%20Additional%20Terms-blue.svg)](LICENSE)
[![Validate](https://img.shields.io/github/actions/workflow/status/AIPMAndy/LivePPT/validate-skill.yml?label=validate)](https://github.com/AIPMAndy/LivePPT/actions/workflows/validate-skill.yml)
[![Stars](https://img.shields.io/github/stars/AIPMAndy/LivePPT?style=social)](https://github.com/AIPMAndy/LivePPT/stargazers)

![LivePPT Demo Preview](assets/demo.gif)

</div>

---

## LivePPT 是什么

LivePPT 不是传统 PPT 工具，也不是单纯的 README 模板。

它更像一个“演示页生成器”：
- 输入 Markdown 内容 / plan
- 一条命令生成 HTML
- 结果可以直接打开、翻页、演示、分享

一句话：**先把内容变成结果，再逐步升级成更高级的演示体验。**

## 适合谁

- 想把项目 README 讲得更清楚的开源作者
- 想快速做产品发布页 / 路演页 / 课程讲义的人
- 不想从零写前端，但又不满足于静态文档的人

## 为什么不是先生成“14 天执行计划”

很多用户第一次来这个项目，是想要：**直接得到 HTML 演示页**。

所以现在的主入口已经调整为：
**内容 -> HTML**

而 `generate_showcase_plan.py` 只是辅助能力，用于：
- 你还没有内容时，先生成一个结构化 plan
- 你想先梳理叙事，再去渲染结果

它不是主价值，更不是唯一入口。

## 30 秒快速开始

```bash
git clone https://github.com/AIPMAndy/LivePPT.git
cd LivePPT
make validate
```

### 最短路径：一条命令生成 HTML

```bash
make build-showcase \
  PROJECT="AI 产品发布网页演示" \
  AUDIENCE="技术决策者" \
  STYLE=neo-luxury \
  BRAND="LivePPT" \
  PLAN=plans/implementation-checklist.md \
  OUTPUT=dist/index.html
```

然后直接打开：

```bash
open dist/index.html
```

### 新增：README 直接生成 HTML deck

如果你已经有现成 README，可以直接：

```bash
make build-from-readme \
  README_INPUT=README.md \
  OUTPUT=dist/readme-deck.html \
  STYLE=prism-command \
  BRAND="LivePPT"
```

这条链路适合：
- 你已经写好了 README
- 你想先快速把现有内容变成演示页
- 你还不想单独维护一份 plan

## 两种常见用法

### 用法 1：我已经有 Markdown / plan，直接生成 HTML

```bash
make render-html \
  PLAN=examples/sample-launch-plan.md \
  OUTPUT=dist/index.html \
  STYLE=cyber-pulse \
  BRAND="LivePPT"
```

适合：
- 已经写好内容
- 只想快速出一个可展示结果

### 用法 2：我还没有内容，先生成 plan 再出 HTML

```bash
python3 scripts/generate_showcase_plan.py \
  --project "AI 产品发布网页演示" \
  --audience "技术决策者" \
  --style "neo-luxury" \
  --output plans/implementation-checklist.md

python3 scripts/render_plan_to_html.py \
  plans/implementation-checklist.md \
  --output dist/index.html \
  --theme neo-luxury \
  --brand "LivePPT"
```

适合：
- 还没想清楚怎么组织页面内容
- 想先拿一个结构化草稿

## 本地查看现成 Demo

```bash
cd demos/liveppt-promo
python3 -m http.server 4188
# open http://localhost:4188
```

## 当前核心能力

- `scripts/build_showcase.py`：一条命令生成 plan + HTML
- `scripts/build_from_readme.py`：直接把 README 渲染成 HTML deck
- `scripts/render_plan_to_html.py`：把 Markdown 渲染为单文件 HTML deck
- `scripts/generate_showcase_plan.py`：生成结构化 plan 草稿
- `scripts/add_theme.py`：生成主题 token CSS
- 支持主题、品牌名、封面副标题参数
- 支持翻页、导航点、进度条、键盘控制

## 常用命令

```bash
# 校验项目
make validate

# 一条命令生成 plan + HTML
make build-showcase \
  PROJECT="AI 产品发布网页演示" \
  AUDIENCE="技术决策者" \
  STYLE=neo-luxury \
  BRAND="LivePPT" \
  PLAN=plans/implementation-checklist.md \
  OUTPUT=dist/index.html

# 用现成 Markdown 直接渲染 HTML
make render-html \
  PLAN=examples/sample-launch-plan.md \
  OUTPUT=dist/index.html \
  STYLE=prism-command \
  BRAND="LivePPT"

# 直接把 README 渲染成 deck
make build-from-readme \
  README_INPUT=README.md \
  OUTPUT=dist/readme-deck.html \
  STYLE=prism-command \
  BRAND="LivePPT"

# 生成主题
python3 scripts/add_theme.py \
  --name midnight-luxe \
  --bg "#09090b" \
  --surface "#15151a" \
  --text "#f4f4f5" \
  --accent "#d4af37" \
  --motion "cubic-bezier(0.22, 1, 0.36, 1)" \
  --output themes/midnight-luxe.css
```

## 当前边界

当前这版已经能解决：
- Markdown / plan / README 直接出 HTML
- 快速得到一个可演示、可分享的结果
- 同一份内容切换不同主题风格

当前还没完全解决：
- 任意 README 无损高保真转演示页
- 复杂布局自动识别
- 一键导出完整静态站资源包
- 更细粒度的页面模板系统

所以现阶段更适合把它理解成：
**“把内容快速变成演示页”的 MVP**，而不是最终形态的全自动发布会引擎。

## 使用场景

- 开源项目发布：把更新日志讲成 6-10 屏故事
- B 端售前演示：同一内容切不同视觉风格
- 课程讲义：把知识点按节奏拆成页面
- 产品介绍：比 README 更有观看路径，比传统 PPT 更轻

## 路线图

- `v0.1.x`：工作流、脚本、文档和 CI 稳定
- `v0.2.x`：继续增强 HTML 输出质量、模板能力、主题系统
- `v0.3.x`：推进 README 直出 deck、更多模板生态、完整静态站导出

详情见 [ROADMAP.md](ROADMAP.md)。

## 开源文档

- [SKILL.md](SKILL.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CHANGELOG.md](CHANGELOG.md)
- [OPEN_SOURCE_LAUNCH_CHECKLIST.md](OPEN_SOURCE_LAUNCH_CHECKLIST.md)
- [releases/v0.1.2.md](releases/v0.1.2.md)
- [releases/distribution-pack-2026-03-03.md](releases/distribution-pack-2026-03-03.md)

## License

`MIT + Additional Terms`（附加条款）

- 中文条款：`LICENSE`
- 英文条款：`LICENSE_EN.md`

---

如果这个项目对你有帮助，欢迎点一个 **Star**，或提一个 Issue 告诉我你最想要的模板能力。
