# Changelog

All notable changes to `dynamic-showcase-web-skill` are documented in this file.

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

- `scripts/generate_showcase_plan.py` 支持 `--mode 7/14`。
- 文档去除绝对路径，提升跨环境可移植性。

## [v0.1.0] - 2026-03-02

### Added

- 首版 skill 工作流与触发规则。
- 设计参考文档、主题风格预设、模板与示例。
- 计划生成与主题生成脚本。
