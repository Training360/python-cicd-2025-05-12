venv:
	python -m venv venv
	pip install -c constraints.txt --editable ".[dev]"

test:
	pytest --cov=calculator --cov-report=html tests

dist:
	python -m build .

upload:
	python -m twine upload --config-file .pypirc dist/*