#!/usr/bin python3

# Liz Lawrens
# New Beginnings 2016
# Final Term Project - ITS CS201
# Decorator Function to check if user is logged in or user session is active

import flask
import functools

def login_required(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'username' in flask.session:
            return method(*args, **kwargs)
        else:
            flask.flash("A login is required.")
            return flask.redirect(flask.url_for('login'))
    return wrapper
