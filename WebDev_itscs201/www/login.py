#!/usr/bin/env python3

# Liz Lawrens
# New Beginnings 2016
# Final Term Project - ITS CS201
# This code contains the login class which renders the login.html for user to login
# When user enters the login details it checks with the entries saved in users.py
# and delivers appropriate message and redirects to the main page

import flask, flask.views
import os
from users import users

class Login(flask.views.MethodView):
    def get(self):
        return flask.render_template('login.html')

    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('main'))
        required = ['username', 'passwd']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('main'))
        username = flask.request.form['username']
        passwd = flask.request.form['passwd']
        if username in users and users[username] == passwd:
            flask.session['username'] = username
        else:
            flask.flash("Username doesn't exist or incorrect password")
        return flask.redirect(flask.url_for('main'))
