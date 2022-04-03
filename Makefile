#!/usr/bin/env python
install:
	poetry install
build:
	poetry build
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest tests/ -v
test-coverage:
	poetry run pytest --cov=gendiff --cov-report=xml tests/
# временные команды для проведения тестов
t:
	python -m pytest --cov=gendiff -v