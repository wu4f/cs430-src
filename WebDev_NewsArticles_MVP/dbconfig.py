from flask_mysqldb import MySQL

def config_mysql(app, db_name):
    # Config MySQL
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = db_name
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init MySQL
def init_mysql(app, db_name):
    config_mysql(app, db_name)
    return MySQL(app)
