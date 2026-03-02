# Contributing

感谢你为 `dynamic-showcase-web-skill` 做贡献。

## 1. Before You Start

- 先阅读 `SKILL.md`，确认改动不破坏触发场景和工作流。
- 新增能力优先做成可复用资源（`scripts/`、`references/`、`assets/`）。
- 涉及视觉与交互改动时，保持“可点击切换 + 多风格切换”主目标不变。

## 2. Contribution Types

- 新主题预设（颜色、字体系、动效曲线）。
- 新场景模板（产品发布、课程讲义、路演等）。
- 新脚本（自动生成计划、主题、检查项等）。
- 文档改进（中文优先，可补充双语）。

## 3. Local Validation

在 skill 根目录执行：

```bash
make validate
python3 scripts/generate_showcase_plan.py --project "Smoke Test" --audience "开发者" --mode 7 --output /tmp/plan.md
python3 scripts/add_theme.py --name smoke --bg "#000" --surface "#111" --text "#fff" --accent "#7c3aed" --motion "ease" --output /tmp/theme.css
python3 scripts/generate_release_note.py --version v0.0.0-smoke --output /tmp/release.md
```

如果你在 monorepo 中使用该 skill，请先 `cd skills/public/dynamic-showcase-web-skill`。

## 4. Pull Request Rules

- PR 标题建议：`feat: ...`、`docs: ...`、`fix: ...`。
- 每个 PR 聚焦一个主题，避免混合无关改动。
- PR 描述至少包含：改动目的、主要变更、验证方式、截图/示例（如适用）。
- 涉及用户体验变化时，必须说明对旧流程的兼容性。

## 5. Style Guidelines

- 中文优先，必要时提供英文补充。
- 文件命名使用小写+短横线。
- 避免引入与本 skill 无关的框架绑定。

## 6. Security

- 禁止提交任何明文 token、密钥、凭据。
- 涉及自动化发布或账号权限的改动，默认要求人工审批。

欢迎通过 Issue 提建议，再通过 PR 共建。
