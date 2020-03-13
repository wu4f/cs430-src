class Model():
    def select(self):
        """
        Gets all rows from the database as a list of lists.
        Row consists of name, email, date, and message.
        :return: List of lists containing all rows of database
        """
        pass

    def insert(self, name, email, message):
        """
        Inserts entry into database
        :param name: String
        :param email: String
        :param message: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
