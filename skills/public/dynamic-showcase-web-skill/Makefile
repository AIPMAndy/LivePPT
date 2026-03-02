PYTHON ?= python3
VERSION ?= v0.1.2

.PHONY: validate release-note

validate:
	$(PYTHON) scripts/validate_skill.py

release-note:
	$(PYTHON) scripts/generate_release_note.py --version $(VERSION)
