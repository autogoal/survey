.PHONY: check
check:
	python scripts/validate_systems.py

.PHONY: dev
dev:
	mkdocs serve &
	find data/* scripts/* | entr python scripts/models_to_markdown.py