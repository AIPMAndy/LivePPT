# Dynamic Showcase Web Skill

Build cinematic click-through web showcases as a premium alternative to static slides.

## What This Skill Solves

- Turns linear slide requests into interactive scene-based web experiences.
- Keeps one narrative while switching multiple visual styles at runtime.
- Uses `SKILL.md` as the single source of truth for workflow and quality rules.

## Current Status (2026-03-02)

- `v0.1.x` 工作流、文档和脚本已可稳定使用。
- 本地校验（`make validate`）和 CI 校验（GitHub Actions）已接通。
- 已具备开源发布基础文档与发布节奏模板。
- `v0.2.0` 规划项（starter 模板、Lighthouse 自动门禁）尚未落地。

## Core Features

- 7/14-day implementation planning (`scripts/generate_showcase_plan.py`).
- Runtime theme generation with token output (`scripts/add_theme.py`).
- One-command local validation (`make validate`).
- Release note scaffolding (`scripts/generate_release_note.py`).

## Repository Structure

```text
dynamic-showcase-web-skill/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── ROADMAP.md
├── OPEN_SOURCE_LAUNCH_CHECKLIST.md
├── Makefile
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── validate-skill.yml
├── scripts/
│   ├── add_theme.py
│   ├── generate_release_note.py
│   ├── generate_showcase_plan.py
│   └── validate_skill.py
├── references/
│   ├── design-system-playbook.md
│   └── style-presets.md
├── assets/
│   └── templates/
│       ├── scene-map.md
│       └── theme-spec.md
├── examples/
│   └── use-cases.md
└── releases/
    ├── v0.1.0.md
    ├── v0.1.1.md
    └── v0.1.2.md
```

## Quick Start

Generate a 14-day implementation plan:

```bash
python3 scripts/generate_showcase_plan.py \
  --project "AI产品发布网页演示" \
  --audience "技术决策者" \
  --mode 14 \
  --style "neo-luxury" \
  --output plans/14-day-plan.md
```

Generate a fast 7-day sprint plan:

```bash
python3 scripts/generate_showcase_plan.py \
  --project "AI产品发布网页演示" \
  --audience "技术决策者" \
  --mode 7 \
  --style "neo-luxury" \
  --output plans/7-day-plan.md
```

Create a new theme token file:

```bash
python3 scripts/add_theme.py \
  --name midnight-luxe \
  --bg "#09090b" \
  --surface "#15151a" \
  --text "#f4f4f5" \
  --accent "#d4af37" \
  --motion "cubic-bezier(0.22, 1, 0.36, 1)" \
  --output themes/midnight-luxe.css
```

## Publish Checklist

- Add one live demo URL.
- Add at least one before/after visual comparison.
- Add release notes with measurable user value.
- Keep theme names and token semantics stable.

## Validate

```bash
make validate
```

Generate next release note template:

```bash
make release-note VERSION=v0.1.3
```

## Open-Source Launch

1. 运行 `make validate`，确保结构与脚本 smoke test 通过。
2. 基于 `releases/v0.1.2.md` 整理首个公开发布说明。
3. 按 `OPEN_SOURCE_LAUNCH_CHECKLIST.md` 完成仓库公开前检查。
4. 创建 tag（如 `v0.1.2`）并发布 release。

## Open Source Docs

- Contributing guide: `CONTRIBUTING.md`
- Roadmap: `ROADMAP.md`
- Changelog: `CHANGELOG.md`
- Open-source launch checklist: `OPEN_SOURCE_LAUNCH_CHECKLIST.md`
- Release notes: `releases/v0.1.0.md`, `releases/v0.1.1.md`, `releases/v0.1.2.md`
- License: `LICENSE`

## License

MIT.
