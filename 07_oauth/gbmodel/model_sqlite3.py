"""
A simple guestbook flask app.
Data is stored in a SQLite database that looks something like the following:

+------------+------------------+------------+-------------+-------------+
| Name       | Email            | signed_on  | message     | picture     |
+============+==================+============+-------------+-------------+
| John Doe   | jdoe@example.com | 2012-05-28 | Hello world | https://... |
+------------+------------------+------------+-------------+-------------+

This can be created with the following SQL (see bottom of this file):

    create table guestbook (name text, email text, signed_on date, message);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from guestbook")
        except sqlite3.OperationalError:
            cursor.execute("create table guestbook (name text, email text, signed_on date, message, picture)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, date, message, picture
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM guestbook")
        return cursor.fetchall()

    def insert(self, name, email, message, picture):
        """
        Inserts entry into database
        :param name: String
        :param email: String
        :param message: String
        :param picture: String        
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'name':name, 'email':email, 'date':date.today(), 'message':message, 'picture':picture}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into guestbook (name, email, signed_on, message, picture) VALUES (:name, :email, :date, :message, :picture)", params)

        connection.commit()
        cursor.close()
        return True
