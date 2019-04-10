.PHONY: clean-pyc clean-build docs clean

TEST_FLAGS=--verbosity=2
COVER_FLAGS=--source=./

help:
	@echo "install - install all requirements including for testing"
	@echo "clean - remove all artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "clean-test-all - remove all test-related artifacts including tox"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-coverage - run tests with coverage report"
	@echo "test-all - run tests on every Python version with tox"
	@echo "check - run all necessary steps to check validity of project"

install:
	pip install -r requirements.txt

clean: clean-build clean-pyc clean-test-all

clean-pyc:
	-@find . -name '*.pyc' -follow -print0 | xargs -0 rm -f
	-@find . -name '*.pyo' -follow -print0 | xargs -0 rm -f
	-@find . -name '__pycache__' -type d -follow -print0 | xargs -0 rm -rf

clean-test:
	rm -rf .coverage coverage*
	rm -rf tests/.coverage test/coverage*
	rm -rf htmlcov/

clean-test-all: clean-test
	rm -rf .tox/

lint:
	flake8 board players

test:
	python manage.py test ${TEST_FLAGS}

test-coverage: clean-test
	-coverage run ${COVER_FLAGS} manage.py test ${TEST_FLAGS}
	@exit_code=$?
	@-coverage report -i
	@-coverage html -i
	@exit ${exit_code}

test-all:
	tox

check: clean-build clean-pyc clean-test lint test