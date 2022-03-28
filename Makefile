#!/usr/bin/env python
install:
	poetry install
build:
	poetry build
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
coverage:
	poetry run pytest --cov=gendiff --cov-report=xml