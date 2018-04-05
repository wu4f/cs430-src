from abc import ABC, abstractmethod

class IModel(ABC):

    """
    Fetch all of the on the entries in the the database.
    @params database_name the name of the the table
    return tuple (nunber of entries, all entries in with the given table name)
    """
    @abstractmethod
    def fetchall(self, database_name):
        pass

    """
    @params username
    return True if the given username in already exists in "user" table
    """
    @abstractmethod
    def user_exists(self, username):
        pass

    """
    Fetch an entry in with an specified id with the given table name.
    @params database_name name of the table
    @params id the given id
    return the specified entry with the given table
    """
    @abstractmethod
    def art(self, database_name, id):
        pass

    """
    Register a user.
    @params values all the require fields requred to register a users
    return True if user was created, False otherwise
    """
    @abstractmethod
    def register_user(self, values):
        pass

    """
    Authenticate users before allows to login.
    @params username the username
    @params password_candidate the password user gave
    return a tuble (Boolean, Boolean), first value if username exists, second is password correct
    """
    @abstractmethod
    def auth_login(self, username, password_candidate):
        pass

    """
    Add article into the table.
    @params values all the field need for adding an article
    return True if the article was added
    """
    @abstractmethod
    def add_art(self, values):
        pass

    """
    Edit an article/comments user wrote.
    @params values the field needed to update the article
    return True if updated in the database
    """
    @abstractmethod
    def update_art(self, values):
        pass

    """
    Delete post/comment user wrote.
    @params id the unique id for the post user wanted to delete
    return True if the post is deleted
    """
    @abstractmethod
    def delete_art(self, id):
        pass
