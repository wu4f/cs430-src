"""
A simple guestbook flask app.
"""
from flask import Flask, redirect, request, url_for, render_template

#from model_sqlite3 import model
from model_pylist import model

app = Flask(__name__)       # our Flask app
model = model()

"""
Function decorator === app.route('/',index())
"""
@app.route('/')
@app.route('/index.html')
def index():
    """
    List guestbook
    """
    entries = [dict(name=row[0], email=row[1], signed_on=row[2], message=row[3] ) for row in model.select()]
    return render_template('index.html', entries=entries)

@app.route('/sign', methods=['POST'])
def sign():
    """
    Accepts POST requests, and processes the form;
    Redirect to index when completed.
    """
    model.insert(request.form['name'], request.form['email'], request.form['message'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
