pipinit:
	pip install -r requirements.txt
	pip install -r requirements_dev.txt

upgrade:
	pip-compile -U requirements.in --resolver=backtracking

format:
	black --exclude '/\.venv/' .
	isort --profile black .

lint:
	flake8 --exclude=.venv/ --ignore=E203,E501,W503
	isort --check-only --profile black .
	black --check --exclude '/\.venv/' .
