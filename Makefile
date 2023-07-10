build:
	poetry build

install:
	poetry install

package-install:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

