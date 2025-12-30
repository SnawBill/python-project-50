build:
	uv build

package-install:
	uv tool install --force dist/*.whl

gendiff:
	uv run gendiff

lint:
	uv run ruff check gendiff

test:
	uv run pytest --cov=gendiff --cov-report=xml