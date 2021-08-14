.PHONY: check
check:
	python scripts/validate.py

.PHONY: dev
dev:
	mkdocs serve &
	find data/* scripts/* | entr python scripts/generate.py