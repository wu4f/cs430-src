from flask import redirect, request, url_for, session
from requests_oauthlib import OAuth2Session
from flask.views import MethodView
from oauth_config import client_id, client_secret, token_url, redirect_callback

class Callback(MethodView):
    def get(self):
        google = OAuth2Session(client_id, redirect_uri = redirect_callback, state=session['oauth_state'])

        # Ensure only HTTPS is utilized
        request.url = request.url.replace('http:','https:')

        # Fetch token from Google's token issuer
        token = google.fetch_token(token_url, client_secret=client_secret,
                            authorization_response=request.url)

        # At this point you can fetch protected resources but lets save
        # the token and show how this is done from a persisted token
        session['oauth_token'] = token

        return redirect(url_for('sign'))
