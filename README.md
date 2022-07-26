# Player selection

## Build the solution
This solution requires Python 3.10 and Poetry 1.1 installed.

To build the solution just install the python dependencies
```shell
poetry install
```

## Run solution locally
To prepare the solution locally (migrate local databse - SQLite), run this command (need to be run only once).
```shell
poetry run python manage.py migrate my_app
```


To run the solution locally (start server on port 3000) just run this command
```shell
poetry run python manage.py runserver 3000
```

Please ignore error messages about unapplying migrations from running the server. The project is initialized from Django app template which includes
irrelevant apps (e.g. `admin`, `auth`, ... etc).

## Run tests
To run the tests just run this command
```shell
poetry run python manage.py test --noinput my_app.tests
```
