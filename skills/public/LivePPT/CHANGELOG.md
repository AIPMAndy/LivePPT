# Changelog

All notable changes to `LivePPT` are documented in this file.

## [Unreleased]

### Added

- 新增 `assets/templates/starter/App.tsx` 与 `styles.css`，提供可点击分镜 starter。
- 新增 `assets/templates/starter/DIFFERENTIATION.md`，明确 anti-clone 约束。
- 新增 starter 使用说明：`assets/templates/starter/README.md`。
- 新增英文许可证：`LICENSE_EN.md`。
- 新增英文文档入口：`README_EN.md`（与中文 README 互链）。
- 新增视觉预览资产：`assets/demo.svg`。
- 新增动态预览资产：`assets/demo.gif`。
- 新增 Issue 模板：`.github/ISSUE_TEMPLATE/bug_report.md`、`feature_request.md`、`config.yml`。
- 新增素材与分发脚本：`scripts/generate_demo_gif.py`、`scripts/generate_distribution_pack.py`。
- 新增分发文案包：`releases/distribution-pack-2026-03-03.md`。

### Changed

- 品牌命名统一为 `LivePPT`（`SKILL.md`、README、workflow、贡献文档等）。
- 新增 `prism-command`、`linen-editorial`、`signal-night` 风格预设。
- 重构 `README.md` 首屏结构，补充对比表、30 秒快速开始、场景与 CTA。
- 修正 promo demo 中的仓库路径与本地运行路径，减少无效跳转。

## [v0.1.2] - 2026-03-02

### Added

- 新增 `CHANGELOG.md` 用于统一记录版本演进。
- 新增 `OPEN_SOURCE_LAUNCH_CHECKLIST.md` 作为开源发布执行清单。
- 新增 `.gitignore`，忽略本地生成产物（`plans/`、`themes/` 等）。

### Changed

- `README.md` 增加当前进度状态与开源发布入口指引。
- CI 的 release-note smoke test 改为输出到 `/tmp`，避免污染工作目录。
- `releases/v0.1.2.md` 填充真实变更项，不再保留空模板。

### Fixed

- 修正旧发布说明中对 `quick_validate.py` 的过时引用。
- 修正部分文档日期与当前发布状态不一致的问题。

## [v0.1.1] - 2026-03-02

### Added

- 新增统一校验脚本：`scripts/validate_skill.py`。
- 新增本地校验入口：`Makefile` + `make validate`。
- 新增 PR 模板：`.github/PULL_REQUEST_TEMPLATE.md`。
- 新增 CI 工作流：`.github/workflows/validate-skill.yml`。

### Changed

- `scripts/generate_showcase_plan.py` 改为输出阶段执行清单，不再依赖固定天数模式。
- 文档去除绝对路径，提升跨环境可移植性。

## [v0.1.0] - 2026-03-02

### Added

- 首版 skill 工作流与触发规则。
- 设计参考文档、主题风格预设、模板与示例。
- 计划生成与主题生成脚本。
