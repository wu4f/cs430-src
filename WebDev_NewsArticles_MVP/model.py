from passlib.hash import sha256_crypt
from IModel import IModel

# from data import Articles
from dbconfig import init_mysql

class AppModel(IModel):
    """docstring for ."""
    def __init__(self, app, name='testing_flask_app'):
        self.arg = app
        self.mysql = init_mysql(app, name)

    def fetchall(self, database_name):
        cur = self.mysql.connection.cursor()
        cmd = "SELECT * FROM {0}".format(database_name)
        result = cur.execute(cmd)
        data = cur.fetchall()
        #close connection
        cur.close()
        return (result, data)

    # True if the username is already exists
    def user_exists(self, username):
        cur = self.mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
        return result > 0

    #Single Article
    def art(self, database_name, id):
        cur = self.mysql.connection.cursor()
        cmd = 'SELECT * FROM {0} WHERE id = {1}'.format(database_name, id)
        result = cur.execute(cmd)
        datum = cur.fetchone()
        cur.close()
        return datum

    def register_user(self, values):
        #create Cursor
        cur = self.mysql.connection.cursor()
        #Execute Query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", values)
        #commit to DB
        self.mysql.connection.commit()
        #close connection
        cur.close()
        return True

    def auth_login(self, username, password_candidate):
        cur = self.mysql.connection.cursor()
        #execute query
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
        if result > 0:
            data = cur.fetchone()
            password = data['password']
            is_pass_valid = sha256_crypt.verify(password_candidate, password)
            return (True, is_pass_valid)
        else:
            return (False, False)

    def add_art(self, values):
        #cursor open
        cur = self.mysql.connection.cursor()
        cur.execute('INSERT INTO articles(title, body, author, link) VALUES(%s, %s, %s, %s)', values)
        cur.connection.commit()
        cur.close()
        return True


    def update_art(self, values):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE articles SET title=%s, body=%s WHERE id = %s", values)
        cur.connection.commit()
        cur.close()
        return True

    def delete_art(self,id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM articles WHERE id = %s",[id])
        self.mysql.connection.commit()
        cur.close()
        return True
