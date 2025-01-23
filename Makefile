install:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check

check: test lint

build:
	uv build

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

package-install:
	uv tool install --force dist/*.whl
