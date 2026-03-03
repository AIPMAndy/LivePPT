[English](README_EN.md) | **简体中文**

<div align="center">

# LivePPT

**把 README 升级为可点击、可切换主题、可发布的动态网页演示。**

[![License](https://img.shields.io/badge/License-MIT%20%2B%20Additional%20Terms-blue.svg)](LICENSE)
[![Validate](https://img.shields.io/github/actions/workflow/status/AIPMAndy/LivePPT/validate-skill.yml?label=validate)](https://github.com/AIPMAndy/LivePPT/actions/workflows/validate-skill.yml)
[![Stars](https://img.shields.io/github/stars/AIPMAndy/LivePPT?style=social)](https://github.com/AIPMAndy/LivePPT/stargazers)

![LivePPT Demo Preview](assets/demo.gif)

</div>

---

## 为什么选 LivePPT

| 能力 | 静态 PPT | 普通 README | **LivePPT** |
|------|:--------:|:-----------:|:-----------:|
| 点击切屏 + 键盘控制 | ⚠️ | ❌ | ✅ |
| 一套内容多主题切换 | ❌ | ❌ | ✅ |
| 发布会叙事分镜 | ⚠️ | ⚠️ | ✅ |
| 脚本化生成工作流 | ❌ | ❌ | ✅ |
| 开源发布配套文档 | ⚠️ | ⚠️ | ✅ |

## 30 秒快速开始

```bash
git clone https://github.com/AIPMAndy/LivePPT.git
cd LivePPT
make validate
```

生成分镜执行清单：

```bash
python3 scripts/generate_showcase_plan.py \
  --project "AI 产品发布网页演示" \
  --audience "技术决策者" \
  --style "neo-luxury" \
  --output plans/implementation-checklist.md
```

本地打开示例 Demo：

```bash
cd demos/liveppt-promo
python3 -m http.server 4188
# open http://localhost:4188
```

## 核心能力

- `scripts/generate_showcase_plan.py`：生成阶段执行清单。
- `scripts/add_theme.py`：快速生成主题 token CSS。
- `scripts/generate_release_note.py`：生成 release note 草稿。
- `scripts/generate_demo_gif.py`：生成可用于 README 的动态预览 GIF。
- `scripts/generate_distribution_pack.py`：生成多平台首发分发文案包。
- `scripts/validate_skill.py`：校验必需文件 + 脚本 smoke test。
- `assets/templates/starter`：可复用 starter（React/Vite）。

## 常用命令

```bash
# 校验
make validate

# 生成主题
python3 scripts/add_theme.py \
  --name midnight-luxe \
  --bg "#09090b" \
  --surface "#15151a" \
  --text "#f4f4f5" \
  --accent "#d4af37" \
  --motion "cubic-bezier(0.22, 1, 0.36, 1)" \
  --output themes/midnight-luxe.css

# 生成下个版本说明模板
make release-note VERSION=v0.1.3

# 生成 README 动态预览图
make demo-gif

# 生成分发文案包
make distribution-pack VERSION=v0.1.3
```

## 场景

- 开源项目发布：把更新日志讲成 6-10 屏发布故事。
- B 端售前演示：同一内容切换成 `neo-luxury` / `prism-command` 等不同风格。
- 课程或知识讲解：用分镜控制节奏，降低信息噪音。

## 路线图

- `v0.1.x`：工作流、脚本、文档和 CI 已稳定。
- `v0.2.0`：补齐 Lighthouse 与响应式质量门禁。
- `v0.3.0`：推进社区模板生态与外部贡献。

详情见 [ROADMAP.md](ROADMAP.md)。

## 开源文档

- [SKILL.md](SKILL.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CHANGELOG.md](CHANGELOG.md)
- [OPEN_SOURCE_LAUNCH_CHECKLIST.md](OPEN_SOURCE_LAUNCH_CHECKLIST.md)
- [releases/v0.1.2.md](releases/v0.1.2.md)
- [releases/distribution-pack-2026-03-03.md](releases/distribution-pack-2026-03-03.md)

## License

`MIT + Additional Terms`（附加条款）。

- 中文条款：`LICENSE`
- 英文条款：`LICENSE_EN.md`

---

如果这个项目对你有帮助，欢迎点一个 **Star**，或提一个 Issue 告诉我你最想要的模板能力。
