setup:
	python3 -m venv ~/project_env && source ~/project_env/bin/activate

install:
	# This should be run from inside a virtualenv
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest

lint:
	pylint app.py

all: install test lint