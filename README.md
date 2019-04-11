# mastermindAPI

Python 3.7 and Django 2.1.7

URLS and usage
--------------

- http://127.0.0.1:8000/players/ for User listing and creation.
- python manage.py changepassword <username> to set a password

- api-auth/ for log in/out
- /movements to interact with movements
- /games to see played Games with its movements and create new Games by clicking in the "extra actions" button or via API
- Inside a game that is not finished you can make a Code gues with "extra actions" button or via API
-

Makefile
--------

Type make command where command can be:

-	"install - install all requirements"
-	"clean - remove all artifacts"
-	"clean-pyc - remove Python file artifacts"
-	"clean-test - remove test and coverage artifacts"
-	"clean-test-all - remove all test-related artifacts including tox"
-	"lint - check style with flake8"
-	"test - run tests quickly with the default Python"
-	"test-coverage - run tests with coverage report"
-	"test-all - run tests on every Python version with tox"
-	"check - run all necessary steps to check validity of project"