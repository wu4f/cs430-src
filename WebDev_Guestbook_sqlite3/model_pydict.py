"""
A simple guestbook flask app.
ata is stored in a SQLite database that looks something like the following:

+------------+------------------+------------+----------------+
| Name       | Email            | signed_on  | message        |
+============+==================+============+----------------+
| John Doe   | jdoe@example.com | 2012-05-28 | Hello world    |
+------------+------------------+------------+----------------+

This can be created with the following SQL (see bottom of this file):

    create table guestbook (name text, email text, signed_on date, message);

"""
from datetime import date
from Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self, app):
        self.guestentries = []

    def select(self):
        """
        Gets all entries from the database
        """
        return self.guestentries

    def insert(self, name, email, message):
        """
        Inserts entry into database
        """
        params = [name, email, date.today(), message]
        self.guestentries.append(params)
