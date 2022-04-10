#!/usr/bin/env python
install:
	poetry install
build:
	poetry build
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest tests/ -vv
test-coverage:
	poetry run pytest --cov=gendiff --cov-report=xml tests/
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*whl
# временные команды для проведения тестов
t:
	python -m pytest --cov=gendiff -v