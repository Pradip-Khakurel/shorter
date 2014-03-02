# Shorter

Shorter is a simple URL Shortener built with Flask and SQLAlchemy named after a famous jazz musician.

## Installation


Install the requirements from the ``requirements.txt`` file:

```
$ pip install -r requirements.txt
```

Then install any python database library you might need for SQLAlchemy e.g. for postgresql:

```
$ pip install psycopg2
```

To initialize the database, first configure the database connection in config.py (you'll have to create the database and user yourself) and then run the ``init_db.py`` script in the project's root directory.

The ``sql_connection`` configuration value in ``config.py`` should be a valid SQLAlchemy database url: http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls

In order to start the server, just run the ``run_server.py`` script in the project's root directory:

```bash
$ ./run_server.py
 * Running on http://127.0.0.1:5000/
```

## Testing

You can run most of the tests from the project's base directory using your favourite python test runner e.g.

```bash
$ python -m unittest discover
```
