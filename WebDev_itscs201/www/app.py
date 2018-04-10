#!/usr/bin/env python3

# Liz Lawrens
# New Beginnings 2016
# Final Term Project - ITS CS201
# This is the application code that runs the entire application.
# It contains different urls to corresponding files that will be 
# called when user clicks on each link/tabs

import flask
import settings
from main import Main
from login import Login
from score import Score
from chapter2 import Chapter2
from chapter3 import Chapter3
from chapter5 import Chapter5
from chapter6 import Chapter6
from chapter8 import Chapter8

app = flask.Flask(__name__)

app.secret_key = settings.secret_key

app.add_url_rule('/', view_func=Main.as_view('main'), methods=['GET','POST'])

app.add_url_rule('/login/', view_func=Login.as_view('login'), methods=['GET', 'POST'])

app.add_url_rule('/score/', view_func=Score.as_view('score'), methods=['GET'])

app.add_url_rule('/chapter2/',view_func=Chapter2.as_view('chapter2'),methods=['GET','POST'])

app.add_url_rule('/chapter3/',view_func=Chapter3.as_view('chapter3'),methods=['GET','POST'])

app.add_url_rule('/chapter5/',view_func=Chapter5.as_view('chapter5'),methods=['GET','POST'])

app.add_url_rule('/chapter6/',view_func=Chapter6.as_view('chapter6'),methods=['GET','POST'])

app.add_url_rule('/chapter8/',view_func=Chapter8.as_view('chapter8'),methods=['GET','POST'])

app.add_url_rule('/<page>/', view_func=Main.as_view('page'), methods=['GET'])

@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'), 404

app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
    #app.run(host='127.0.0.1',port=5000)
