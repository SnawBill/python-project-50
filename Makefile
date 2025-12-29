build:
	uv build

package-install:
	uv tool install --force dist/*.whl

gendiff:
	uv run gendiff