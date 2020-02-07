"""
A simple guestbook flask application.
"""
import flask
from flask.views import MethodView
from index import Index
from sign import Sign

application = flask.Flask(__name__)       # our Flask app

application.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

application.add_url_rule('/sign/',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
