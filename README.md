# mastermindAPI


URLS and usage
--------------

- http://127.0.0.1:8000/players/ for user listing and creation
and python manage.py changepassword <username> to create a password
- api-auth/ for log in/out
- /movements to interact with movements
- /games to interact with games


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