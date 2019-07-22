import functools
import os
import json

import flask

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth

app  = flask.Flask(__name__)
app.secret_key = os.getenv("FN_FLASK_SECRET_KEY", default=False)

app.register_blueprint(google_auth.app)

@app.route('/')
def index():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        # Allow only elucidata logins
        if user_info.has_key('hd') and user_info['hd'] == 'elucidata.io':
            return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"
        else:
            google_auth.logout()
            return '<div>You are not allowed to sign-in</div>'
    return 'You are not currently logged in.'

