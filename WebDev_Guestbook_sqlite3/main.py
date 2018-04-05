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
from flask import Flask, redirect, request, url_for, render_template

import sqlite3

app = Flask(__name__)       # our Flask app
DB_FILE = 'entries.db'    # file for our Database

def select():
    """
    Gets all entries from the database
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM guestbook")
    return cursor.fetchall()

def insert(name, email, message):
    """
    Inserts entry into database
    """
    params = {'name':name, 'email':email, 'date':date.today(), 'message':message}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("insert into guestbook (name, email, signed_on, message) VALUES (:name, :email, :date, :message)", params)

    connection.commit()
    cursor.close()

"""
Function decorator === app.route('/',index())
"""
@app.route('/')
@app.route('/index.html')
def index():
    """ 
    List guestbook
    """
    entries = [dict(name=row[0], email=row[1], signed_on=row[2], message=row[3] ) for row in select()]
    return render_template('index.html', entries=entries)

@app.route('/sign', methods=['POST'])
def sign():
    """
    Accepts POST requests, and processes the form;
    Redirect to index when completed.
    """
    insert(request.form['name'], request.form['email'], request.form['message']) 
    return redirect(url_for('index'))

if __name__ == '__main__':

    # Make sure our database exists
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    try:
        cursor.execute("select count(rowid) from guestbook")
    except sqlite3.OperationalError:
        cursor.execute("create table guestbook (name text, email text, signed_on date, message)")
    cursor.close()

    app.run(host='0.0.0.0', debug=True)
