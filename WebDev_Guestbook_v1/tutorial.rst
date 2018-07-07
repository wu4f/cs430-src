Flask Tutorial (mempy)
======================

A simple introduction to `Flask <http://flask.pocoo.org/docs/quickstart/>`_

Installation::

    pip install flask

Hello World
-----------

A simple hello world app (``hello.py``)::

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run()

Run the server::
    
    python hello.py

Now, run in Debug Mode, and allow anyone on the network to connect::

    app.run(host='0.0.0.0', debug=True)

Add a new/different route and function/page::
        
    @app.route('/profile/<username>')
    def profile(username):
        return "Welcome to {u}'s profile".format(u=username)

Add a converter for variable parameters in the URL::

    @app.route('/add-five/<int:num>')
    def add_five(num):
        return "{n} + 6 = {val}".format(n=num, val=num+5)


A Guestbook
-----------

OR, *Welcome to 1997*.


Create the directory structure::

    /guestbook
        /templates

We'll put our application in the ``guestbook`` directory, and we'll write some
HTML templates (using `Jinja2 <http://jinja.pocoo.org/docs/templates/>`_), which
go in the ``templates`` directory.

First, we'll write a couple of simple functions that store and retrieve data in
an SQLite database. Our database contains a table called ``guestbook``, which
contains three columns:  ``name``, ``email``, and ``signed_on`` which is a date.

The first function, pulls all data from this table::

    def _select():
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM guestbook")
        return cursor.fetchall()

A function to save a ``name`` and ``email``::

    def _insert(name, email):
        """
        put a new entry in the database
        """
        params = {'name':name, 'email':email, 'date':date.today()}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        
        cursor.execute("insert into guestbook (name, email, signed_on) VALUES (:name, :email, :date)", params)

        connection.commit()
        cursor.close()

A flask *view* to list everyone that's signed the guestbook::

    @app.route('/')
    def index():
        """ 
        List everyone who's signed the guestbook 
        
        """
        entries = [dict(name=row[0], email=row[1], signed_on=row[2] ) for row in _select()]
        return render_template('index.html', entries=entries)

Some templates... The first is ``layout.html`` which defines the *top-level*
html document. This is a Jinja2 template::

    <!doctype html>
    <html>
    <title>Guestbook</title>
    <link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
    <div class=page>
        <h1>Guestbook</h1>
        {% block content %}{% endblock %}
        </div>

And now the bit of html that's used in the ``index`` view. This also contains a
form that will be used to sign the guestbook. This goes in ``main.py``::

    {% extends "layout.html" %}
    {% block content %}
        
        <form action="{{ url_for('sign') }}" method=post>
          <dl>
            <dt>Name
            <dd><input type=text name=name>
            <dt>Email:
            <dd><input type=text name=email>
            <dd><input type=submit value=Sign>
          </dl>
        </form>

        <h2>Signatures</h2>
        {% for entry in entries %}
            <p class=entry>
                {{ entry.name }} &lt;{{ entry.email }}&gt;
                <br>signed on {{ entry.signed_on }}
            </p>
        {% else %}
            <p class=entry>What!? Nobody's signed!</p>
        {% endfor %}
    {% endblock %}

Now, how do we process this form when it's submitted? We'll create a ``sign`` 
view in ``main.py``::

    @app.route('/sign', methods=['POST'])
    def sign():
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        _insert(request.form['name'], request.form['email']) 
        return redirect(url_for('index'))

Finally... let's put it all together, defining our main flask app::

    if __name__ == '__main__':

        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from guestbook")
        except sqlite3.OperationalError:
            cursor.execute("create table guestbook (name text, email text, signed_on date)")
        cursor.close()
            
        # Answer queries for any client, With DEBUG mode turned on!
        app.run(host='0.0.0.0', debug=True)


