import sqlite3
from flask import g

import os
DATABASE = 'test-db.sqlite'

# Connect to the database.
def connect_db():
    db_path = os.path.join(os.getcwd(), DATABASE)
    if not os.path.isfile(db_path):
        raise RuntimeError("Can't find database file '{}'".format(db_path))
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection

# Open a database connection and hang on to it in the global object.
def open_db_connection():
    g.db = connect_db()

# If the database is open, close it.
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
