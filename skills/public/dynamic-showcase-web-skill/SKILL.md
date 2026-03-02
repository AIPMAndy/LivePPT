---
name: dynamic-showcase-web-skill
description: Build click-through cinematic web showcase pages with dynamic transitions and runtime style switching. Use when users ask for PPT alternatives, interactive launch pages, or high-end storytelling websites with multiple visual styles.
---

# Dynamic Showcase Web Skill

## Overview

把线性 PPT 请求升级为“点击切换的动态网页演示”。
默认产出中文内容，支持多主题切换、电影感转场、场景化叙事和可部署 Demo。

## Trigger Scenarios

- 用户说“不要传统 PPT，要网页演示、可点击翻页、酷炫高级感”。
- 用户要“同一份内容切换不同视觉风格（商务/科技/极简）”。
- 用户要“产品发布页、路演页、课程讲义页、案例展示页”且强调互动感。
- 用户要“开源模板 + 演示站 + 可复用主题系统”。

## Input Contract

先收集以下最小输入：
- 主题和目标受众（例如“AI 产品发布给技术决策者”）。
- 场景数量（建议 6-12 屏）。
- 视觉偏好（如 `neo-luxury`、`cyber-pulse`、`minimal-editorial`）。
- 必须展示的信息（产品亮点、数据、CTA、联系入口）。

## Workflow

### Step 1: Define Narrative Spine

- 输出一句话叙事：`谁在什么场景下遇到什么问题，我们如何带来可量化结果`。
- 固定页面结构：封面 -> 痛点 -> 方案 -> 证据 -> 架构 -> 价格/计划 -> CTA。
- 每屏只承载一个核心信息点，减少信息噪音。

### Step 2: Scaffold Project

- 默认技术栈：`React + Vite + Framer Motion + CSS Variables`。
- 使用 `scripts/generate_showcase_plan.py` 先产出执行清单（支持 `--mode 7/14`）。
- 根据风格需求建立主题令牌：`color`, `typography`, `radius`, `shadow`, `motion`。

### Step 3: Build Scene System

- 页面抽象为 `Scene` 组件，统一支持进入/退出动效。
- 必须支持三种切换方式：点击按钮、键盘方向键、目录跳转。
- 提供进度指示器与“当前屏序号/总屏数”。

### Step 4: Implement Theme Switching

- 主题使用 CSS 变量和 `data-theme` 驱动。
- 风格切换不改文案和结构，只替换视觉令牌和动效参数。
- 使用 `scripts/add_theme.py` 生成新主题变量文件。

### Step 5: Add Premium Motion

- 必选动画：页面过渡、元素分层入场、hover 反馈。
- 可选动画：视差、光晕、3D rotate、颗粒背景。
- 控制节奏：默认 350-700ms，避免过快或眩晕。

### Step 6: QA and Publish

- 校验移动端和桌面端适配。
- Lighthouse 目标：Performance >= 85, Accessibility >= 90。
- 产出 Demo 链接和 README 截图/GIF 后再发布。

## Quality Bar

- 视觉一致性：同一主题内颜色、字体、阴影语义稳定。
- 交互一致性：所有 Scene 切换逻辑一致，避免跳屏。
- 可访问性：文本对比度达标，提供 `prefers-reduced-motion` 降级。
- 可复用性：新主题可以在 10 分钟内接入现有场景。

## AI Delegation

- AI 主导：结构草案、文案压缩、组件骨架、主题变量生成。
- 人类主导：品牌调性、最终审美判断、公开发布文案。
- AI 辅助：性能优化建议、动效微调建议、KPI 复盘建议。

## Standard Deliverables

- `showcase-outline.md`：逐屏大纲和核心信息。
- `theme-spec.md`：主题令牌定义和视觉说明。
- `demo-url`：可在线访问的演示页面。
- `release-note.md`：版本更新与用户价值说明。

## Resources (optional)

### scripts/
- `scripts/generate_showcase_plan.py`：生成 7/14 天构建与发布计划。
- `scripts/add_theme.py`：根据参数生成主题 CSS 变量文件。
- `scripts/generate_release_note.py`：生成版本发布说明模板。
- `scripts/validate_skill.py`：执行必需文件检查和脚本 smoke test。

### references/
- `references/design-system-playbook.md`：设计与动效规范。
- `references/style-presets.md`：预设主题定义与适配建议。

### assets/
- `assets/templates/scene-map.md`：场景结构模板。
- `assets/templates/theme-spec.md`：主题定义模板。

### examples/
- `examples/use-cases.md`：路演、课程、产品发布三类示例请求。
