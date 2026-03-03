<div align="center">

# 🎬 LivePPT

**把 PPT 变成电影级网页演示 — 点击翻页、主题切换、动态转场**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](skills/public/LivePPT/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/AIPMAndy/LivePPT?style=social)](https://github.com/AIPMAndy/LivePPT)

[English](#english) | **简体中文**

<img src="skills/public/LivePPT/assets/demo.gif" width="680" alt="LivePPT Demo">

*（Demo GIF 待补）*

</div>

---

## 🆚 为什么选 LivePPT？

| 能力 | Reveal.js | Slidev | Marp | **LivePPT** |
|------|:---------:|:------:|:----:|:-----------:|
| 点击式场景切换 | ✅ | ✅ | ❌ | ✅ |
| 运行时主题切换 | ❌ | 部分 | ❌ | ✅ **秒切** |
| 电影感转场动效 | 基础 | 基础 | ❌ | ✅ **内置多款** |
| 移动端适配 | 需配置 | 需配置 | ✅ | ✅ **默认适配** |
| 设计系统集成 | ❌ | ❌ | ❌ | ✅ **令牌驱动** |
| AI 生成计划 | ❌ | ❌ | ❌ | ✅ **7/14天计划** |

**一句话差异**：传统幻灯片工具是"翻页"，LivePPT 是"沉浸式讲故事"。

---

## 🚀 30 秒快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/AIPMAndy/LivePPT.git
cd LivePPT/skills/public/LivePPT

# 2. 生成 14 天执行计划
python3 scripts/generate_showcase_plan.py \
  --project "AI产品发布" \
  --audience "技术决策者" \
  --mode 14 \
  --style "neo-luxury" \
  --output plans/my-plan.md

# 3. 创建自定义主题
python3 scripts/add_theme.py \
  --name midnight-luxe \
  --bg "#09090b" \
  --accent "#d4af37" \
  --output themes/midnight-luxe.css

# 4. 校验项目结构
make validate
```

---

## ✨ 核心功能

### 🎭 运行时主题切换
同一份内容，一键切换 `neo-luxury` / `cyber-pulse` / `minimal-editorial` 等风格，演示时按受众调整。

### 🎥 电影感转场
内置 Framer Motion 动效系统：分层入场、视差滚动、光晕效果、3D 旋转。节奏控制在 350-700ms，避免眩晕。

### 📱 移动端优先
默认响应式适配，支持触屏滑动、方向键、点击按钮三种切换方式。

### 🤖 AI 辅助构建
| 脚本 | 功能 |
|------|------|
| `generate_showcase_plan.py` | 输入主题+受众 → 7/14 天执行清单 |
| `add_theme.py` | 输入配色 → 完整 CSS 变量文件 |
| `validate_skill.py` | 一键校验项目结构 |
| `generate_release_note.py` | 生成版本发布说明 |

---

## 💡 使用场景

| 场景 | 传统方案 | LivePPT 方案 |
|------|----------|--------------|
| **产品发布** | 静态 PPT + 截图 | 可交互演示站，实时切主题 |
| **投资路演** | 幻灯片念稿 | 电影感叙事，数据动态入场 |
| **课程讲义** | PDF 导出 | 在线互动，学员自行翻阅 |
| **案例展示** | Word 文档 | 视觉冲击力强的作品集 |

---

## 📦 项目结构

```
LivePPT/
├── README.md                        # 本文件
└── skills/public/LivePPT/
    ├── SKILL.md                     # Agent 技能定义
    ├── scripts/                     # 自动化脚本
    │   ├── generate_showcase_plan.py
    │   ├── add_theme.py
    │   └── validate_skill.py
    ├── references/                  # 设计规范
    │   ├── design-system-playbook.md
    │   └── style-presets.md
    ├── assets/templates/starter/    # 起步模板
    └── releases/                    # 版本记录
```

---

## 🗺️ Roadmap

- [x] v0.1.x — 核心工作流 + 脚本 + CI 校验
- [x] 预设主题：neo-luxury, cyber-pulse, minimal-editorial
- [ ] v0.2.0 — Lighthouse 自动门禁
- [ ] v0.3.0 — 在线主题编辑器
- [ ] v1.0.0 — Figma 插件 + 一键导出

---

## 🤝 贡献

欢迎 PR！详见 [CONTRIBUTING.md](skills/public/LivePPT/CONTRIBUTING.md)

**可以贡献的内容：**
- 新主题预设（颜色 / 字体 / 动效）
- 新场景模板（路演 / 课程 / 发布会）
- 脚本增强（校验、发布、文档生成）

---

## 👨‍💻 作者

**AI酋长Andy** | 前腾讯/百度 AI 产品专家，AI 商业战略顾问

[![微信](https://img.shields.io/badge/微信-AIPMAndy-07C160?logo=wechat&logoColor=white)](https://your-wechat-qr-link)
[![GitHub](https://img.shields.io/badge/GitHub-AIPMAndy-181717?logo=github)](https://github.com/AIPMAndy)

---

## 📄 License

[Apache 2.0 + 附加条款](skills/public/LivePPT/LICENSE)

✅ **允许**：个人学习、企业内部使用、开源引用（需保留作者信息）

❌ **禁止**（除非书面授权）：去品牌化、商业 SaaS、转售/倒卖

商业授权联系：微信 AIPMAndy

---

<div align="center">

**如果有帮助，请给个 ⭐ Star！**

</div>

---

## English

**Transform slides into cinematic web showcases — click-through, theme switching, dynamic transitions**

### Why LivePPT?

| Capability | Reveal.js | Slidev | Marp | **LivePPT** |
|------------|:---------:|:------:|:----:|:-----------:|
| Click-through scenes | ✅ | ✅ | ❌ | ✅ |
| Runtime theme switching | ❌ | Partial | ❌ | ✅ **Instant** |
| Cinematic transitions | Basic | Basic | ❌ | ✅ **Built-in** |
| Mobile responsive | Config needed | Config needed | ✅ | ✅ **Default** |
| Design system integration | ❌ | ❌ | ❌ | ✅ **Token-driven** |
| AI-generated plans | ❌ | ❌ | ❌ | ✅ **7/14-day** |

**The difference**: Traditional slides = "page turns." LivePPT = "immersive storytelling."

### Quick Start

```bash
git clone https://github.com/AIPMAndy/LivePPT.git
cd LivePPT/skills/public/LivePPT
make validate
```

### License

[Apache 2.0 + Additional Terms](skills/public/LivePPT/LICENSE)

**Allowed**: Personal learning, internal enterprise use, open-source citation (retain author attribution)

**Prohibited** (without written authorization): De-branding, commercial SaaS, resale

Commercial licensing: WeChat AIPMAndy
