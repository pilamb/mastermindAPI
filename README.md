# mastermindAPI

What?
-----

This is a DjangoREST API to play [mastermind](https://es.wikipedia.org/wiki/Mastermind) against the machine.

An anonymous user can create Users, and when loged in users can make login and start a game, check his game history including movements.
The backend will respond with jsons with results like: "you won", "you loose",
and when in a game "black pegs: int, white pegs: int".
If a game is finished no more codes can be sent.

Made with Python 3.7 and Django 2.1.7.


Quick start
-----------

0) Use virtualenv to stock this repo or use Docker (see "Docker" below)
1) Install modules needed:```pip install -r requirements.txt``` or ```make install```
2) Start the backend: ```python manage.py runserver```
3) Visit http://127.0.0.1:8000


Users management and creation
-----------------------------

Authentication is required except for Player management:

- http://127.0.0.1:8000/players/ for User creation.
- python manage.py changepassword <username> to set a password


URLs
----

- api-auth/ for log in/out
- /movements to interact with movements
- /games to see played Games with its movements and create new Games by clicking in the "extra actions" button or via API
- Inside a game detail (such as games/3/) that is not finished, you can make a Code guess with "extra actions" button or via API
- Example: http://192.168.99.100:8000/games/15/play/ and insert a code. Feedback will be answered.

Docker
------

docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up


Makefile
--------

Type "make command" where command can be:

-	"install - install all requirements"
-	"clean - remove all artifacts"
-	"clean-pyc - remove Python file artifacts"
-	"clean-test - remove test and coverage artifacts"
-	"clean-test-all - remove all test-related artifacts including tox"
-	"lint - check style with flake8"
-	"test - run tests quickly with the default Python"
-	"test-coverage - run tests with coverage report"
-	"check - run all necessary steps to check validity of project"
