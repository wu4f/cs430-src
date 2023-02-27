"""
A simple guestbook flask app.
Data is stored in a SQLite database that looks something like the following:

+------------+------------------+---------------------+----------------+
| Name       | Email            | signed_on           | message        |
+============+==================+=====================+================+
| John Doe   | jdoe@example.com | 2012-05-28 12:00:22 | Hello world    |
+------------+------------------+---------------------+----------------+

This can be created with the following SQL (see bottom of this file):

    create table entries (name text, email text, signed_on timestamp, message text);

"""
from datetime import datetime
from .model import Model
import psycopg
import os
from dotenv import load_dotenv
load_dotenv()

DB_CONNECTION = "host=%s port=%s dbname=%s user=%s password=%s" % (os.getenv('DB_HOST'), os.getenv('DB_PORT'), os.getenv('DB_NAME'), os.getenv('DB_USER'), os.getenv('DB_PASS'))

class ModelSqlPostgres(Model):
    def __init__(self):
        # Make sure our database exists
        with psycopg.connect(DB_CONNECTION) as connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute("SELECT count(*) FROM entries")
                except psycopg.errors.UndefinedTable:
                    connection.rollback()
                    cursor.execute("CREATE TABLE entries (id serial, name text, email text, signed_on timestamp, message text)")
                    connection.commit()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, signed_on, message, id
        :return: List of lists containing all rows of database
        """
        with psycopg.connect(DB_CONNECTION) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT name, email, signed_on, message, id FROM entries")
                return cursor.fetchall()

    def insert(self, name, email, message):
        """
        Inserts entry into database
        :param name: String
        :param email: String
        :param message: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'name':name, 'email':email, 'datetime':datetime.now(), 'message':message}
        with psycopg.connect(DB_CONNECTION) as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO entries (name, email, signed_on, message) VALUES (%(name)s, %(email)s, %(datetime)s, %(message)s)", params)
                connection.commit()
        return True
