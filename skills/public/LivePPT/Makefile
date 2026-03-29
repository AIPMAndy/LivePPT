PYTHON ?= python3
VERSION ?= v0.1.2
PLAN ?= examples/sample-launch-plan.md
OUTPUT ?= dist/index.html
PROJECT ?= AI 产品发布网页演示
AUDIENCE ?= 技术决策者
STYLE ?= neo-luxury
BRAND ?= LivePPT
README_INPUT ?= README.md

.PHONY: validate release-note demo-gif distribution-pack render-html build-showcase build-from-readme

validate:
	$(PYTHON) scripts/validate_skill.py

render-html:
	$(PYTHON) scripts/render_plan_to_html.py $(PLAN) --output $(OUTPUT) --theme $(STYLE) --brand "$(BRAND)"

build-showcase:
	$(PYTHON) scripts/build_showcase.py --project "$(PROJECT)" --audience "$(AUDIENCE)" --style $(STYLE) --brand "$(BRAND)" --plan-output $(PLAN) --html-output $(OUTPUT)

build-from-readme:
	$(PYTHON) scripts/build_from_readme.py $(README_INPUT) --output $(OUTPUT) --theme $(STYLE) --brand "$(BRAND)"

release-note:
	$(PYTHON) scripts/generate_release_note.py --version $(VERSION)

demo-gif:
	$(PYTHON) scripts/generate_demo_gif.py --output assets/demo.gif

distribution-pack:
	$(PYTHON) scripts/generate_distribution_pack.py --version $(VERSION)
