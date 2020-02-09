mypy:
	poetry run mypy scatterping

flake8:
	poetry run flake8 scatterping

lint: mypy flake8
