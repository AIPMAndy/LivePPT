PYTHON ?= python3
VERSION ?= v0.1.2
PLAN ?= examples/sample-launch-plan.md
OUTPUT ?= dist/index.html

.PHONY: validate release-note demo-gif distribution-pack render-html

validate:
	$(PYTHON) scripts/validate_skill.py

render-html:
	$(PYTHON) scripts/render_plan_to_html.py $(PLAN) --output $(OUTPUT)

release-note:
	$(PYTHON) scripts/generate_release_note.py --version $(VERSION)

demo-gif:
	$(PYTHON) scripts/generate_demo_gif.py --output assets/demo.gif

distribution-pack:
	$(PYTHON) scripts/generate_distribution_pack.py --version $(VERSION)
