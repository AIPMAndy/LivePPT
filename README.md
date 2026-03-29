<div align="center">

# 🎬 LivePPT

**把 Markdown / README 变成可点击、可翻页、可分享的 HTML 演示页。**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](skills/public/LivePPT/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/AIPMAndy/LivePPT?style=social)](https://github.com/AIPMAndy/LivePPT)

**简体中文**

<img src="skills/public/LivePPT/assets/demo.gif" width="680" alt="LivePPT Demo">

</div>

---

## LivePPT 是什么

LivePPT 不是传统 PPT 工具，也不是单纯的 README 模板。

它更像一个“演示页生成器”：
- 输入 Markdown 内容 / README
- 一条命令生成 HTML
- 结果可以直接打开、翻页、演示、分享

一句话：**先把内容变成结果，再逐步升级成更高级的演示体验。**

## 为什么用它

| 能力 | 静态 PPT | 普通 README | **LivePPT** |
|------|:--------:|:-----------:|:-----------:|
| 直接生成 HTML 演示页 | ❌ | ❌ | ✅ |
| 点击翻页 + 键盘控制 | ⚠️ | ❌ | ✅ |
| 一套内容切换不同主题风格 | ❌ | ❌ | ✅ |
| README 直接转演示页 | ❌ | ❌ | ✅ |
| 轻量脚本化工作流 | ⚠️ | ❌ | ✅ |

## 30 秒快速开始

```bash
git clone https://github.com/AIPMAndy/LivePPT.git
cd LivePPT/skills/public/LivePPT
make validate
```

### 最短路径：现成 README 直接生成 HTML

```bash
make build-from-readme \
  README_INPUT=README.md \
  OUTPUT=dist/readme-deck.html \
  STYLE=prism-command \
  BRAND="LivePPT"
```

然后直接打开：

```bash
open dist/readme-deck.html
```

### 如果你没有内容，再一条命令生成 HTML

```bash
make build-showcase \
  PROJECT="AI 产品发布网页演示" \
  AUDIENCE="技术决策者" \
  STYLE=neo-luxury \
  BRAND="LivePPT" \
  PLAN=plans/showcase.md \
  OUTPUT=dist/index.html
```

## 当前核心能力

- `build-from-readme`：README 直接生成 HTML deck
- `build-showcase`：一条命令生成 Markdown 内容 + HTML
- `render_plan_to_html.py`：把 Markdown 渲染为单文件 HTML deck
- `add_theme.py`：生成主题 token CSS
- 支持主题、品牌名、封面副标题参数
- 支持翻页、导航点、进度条、键盘控制

## 适合场景

- 开源项目发布：把 README / 更新日志变成演示页
- 产品发布：快速做可讲解、可分享的网页演示
- B 端售前：同一内容切不同视觉风格
- 课程讲义：把知识内容拆成节奏化页面

## 项目结构

```bash
LivePPT/
├── README.md
└── skills/public/LivePPT/
    ├── README.md
    ├── SKILL.md
    ├── scripts/
    │   ├── build_from_readme.py
    │   ├── build_showcase.py
    │   ├── render_plan_to_html.py
    │   ├── generate_showcase_plan.py
    │   └── add_theme.py
    ├── demos/
    ├── examples/
    ├── references/
    └── releases/
```

## 当前边界

当前这版已经能解决：
- Markdown / README 直接出 HTML
- 快速得到一个可演示、可分享的结果
- 同一份内容切换不同主题风格

当前还没完全解决：
- 任意 README 无损高保真转发布会页面
- 复杂布局自动识别
- 一键导出完整静态站资源包
- 更细粒度的页面模板系统

所以现阶段更适合把它理解成：
**“把内容快速变成演示页”的 MVP**。

## 更多文档

- Skill 文档：`skills/public/LivePPT/README.md`
- 技能定义：`skills/public/LivePPT/SKILL.md`
- 贡献说明：`skills/public/LivePPT/CONTRIBUTING.md`
- 路线图：`skills/public/LivePPT/ROADMAP.md`

## License

[Apache 2.0 + 附加条款](skills/public/LivePPT/LICENSE)

✅ 允许：个人学习、企业内部使用、开源引用（保留作者信息）

❌ 禁止（除非书面授权）：去品牌化、商业 SaaS、转售 / 倒卖

商业授权联系：微信 AIPMAndy

---

<div align="center">

**如果这个项目对你有帮助，欢迎点个 ⭐ Star**

</div>
