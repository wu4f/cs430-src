"""
Python dictionary model
"""
from datetime import date
from . import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        self.gbentries = []

    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        return self.gbentries

    def insert(self, name, email, message):
        """
        Inserts entry into database
        :param name: String
        :param email: String
        :param message: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        params = [name, email, date.today(), message]
        self.gbentries.append(params)
