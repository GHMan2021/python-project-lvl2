#!/usr/bin/env python
install:
	poetry install
build:
	poetry build
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest test/
test-coverage:
	poetry run pytest --cov=tests/ --cov-report=xml