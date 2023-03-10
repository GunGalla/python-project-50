install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

start:
	poetry run

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint test

.PHONY: install
