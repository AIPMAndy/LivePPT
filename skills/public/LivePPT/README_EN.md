**English** | [简体中文](README.md)

<div align="center">

# LivePPT

**Turn your README into a clickable, theme-switchable, launch-ready web showcase.**

[![License](https://img.shields.io/badge/License-MIT%20%2B%20Additional%20Terms-blue.svg)](LICENSE)
[![Validate](https://img.shields.io/github/actions/workflow/status/AIPMAndy/LivePPT/validate-skill.yml?label=validate)](https://github.com/AIPMAndy/LivePPT/actions/workflows/validate-skill.yml)
[![Stars](https://img.shields.io/github/stars/AIPMAndy/LivePPT?style=social)](https://github.com/AIPMAndy/LivePPT/stargazers)

![LivePPT Demo Preview](assets/demo.gif)

</div>

---

## Why LivePPT

| Capability | Static Slides | Plain README | **LivePPT** |
|-----------|:-------------:|:------------:|:-----------:|
| Click-through + keyboard navigation | ⚠️ | ❌ | ✅ |
| One narrative, multiple visual themes | ❌ | ❌ | ✅ |
| Launch-style scene storytelling | ⚠️ | ⚠️ | ✅ |
| Scripted workflow generation | ❌ | ❌ | ✅ |
| Open-source launch docs included | ⚠️ | ⚠️ | ✅ |

## 30-Second Quick Start

```bash
git clone https://github.com/AIPMAndy/LivePPT.git
cd LivePPT
make validate
```

Generate a stage-based implementation checklist:

```bash
python3 scripts/generate_showcase_plan.py \
  --project "AI Product Launch Web Showcase" \
  --audience "Technical Decision Makers" \
  --style "neo-luxury" \
  --output plans/implementation-checklist.md
```

Run the promo demo locally:

```bash
cd demos/liveppt-promo
python3 -m http.server 4188
# open http://localhost:4188
```

## Core Capabilities

- `scripts/generate_showcase_plan.py`: stage checklist generator.
- `scripts/add_theme.py`: theme token CSS generator.
- `scripts/generate_release_note.py`: release note scaffold.
- `scripts/generate_demo_gif.py`: lightweight animated preview generator for README.
- `scripts/generate_distribution_pack.py`: multi-channel launch copy generator.
- `scripts/validate_skill.py`: required-file and smoke-test validator.
- `assets/templates/starter`: reusable React/Vite starter template.

## Common Commands

```bash
# Validate required docs and scripts
make validate

# Create a new theme token file
python3 scripts/add_theme.py \
  --name midnight-luxe \
  --bg "#09090b" \
  --surface "#15151a" \
  --text "#f4f4f5" \
  --accent "#d4af37" \
  --motion "cubic-bezier(0.22, 1, 0.36, 1)" \
  --output themes/midnight-luxe.css

# Generate next release note template
make release-note VERSION=v0.1.3

# Generate README animated preview
make demo-gif

# Generate launch distribution copy pack
make distribution-pack VERSION=v0.1.3
```

## Use Cases

- Open-source launch storytelling with 6-10 scenes.
- B2B pitching with style switching (`neo-luxury`, `prism-command`, etc.).
- Interactive course or knowledge walkthroughs with controlled pacing.

## Roadmap

- `v0.1.x`: workflow, scripts, docs, and CI are production-ready.
- `v0.2.0`: add Lighthouse and responsive quality gates.
- `v0.3.0`: grow a community-driven template ecosystem.

See [ROADMAP.md](ROADMAP.md) for details.

## Open Source Docs

- [SKILL.md](SKILL.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CHANGELOG.md](CHANGELOG.md)
- [OPEN_SOURCE_LAUNCH_CHECKLIST.md](OPEN_SOURCE_LAUNCH_CHECKLIST.md)
- [releases/v0.1.2.md](releases/v0.1.2.md)
- [releases/distribution-pack-2026-03-03.md](releases/distribution-pack-2026-03-03.md)

## License

`MIT + Additional Terms`.

- Chinese terms: `LICENSE`
- English terms: `LICENSE_EN.md`

---

If this project helps you, please give it a **Star** or open an Issue with your most wanted template capability.
