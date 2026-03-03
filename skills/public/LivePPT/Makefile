PYTHON ?= python3
VERSION ?= v0.1.2

.PHONY: validate release-note demo-gif distribution-pack

validate:
	$(PYTHON) scripts/validate_skill.py

release-note:
	$(PYTHON) scripts/generate_release_note.py --version $(VERSION)

demo-gif:
	$(PYTHON) scripts/generate_demo_gif.py --output assets/demo.gif

distribution-pack:
	$(PYTHON) scripts/generate_distribution_pack.py --version $(VERSION)
