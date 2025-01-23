install:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check

check: test lint

build:
	uv build

package-install:
	uv tool install --force dist/*.whl
