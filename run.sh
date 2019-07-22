export FN_AUTH_REDIRECT_URI=http://localhost:8040/google/auth
export FN_BASE_URI=http://localhost:8040
export FN_CLIENT_ID=GOGOLE_AUTH_CLIENT_ID
export FN_CLIENT_SECRET=GOGOLE_AUTH_SECRET_ID

export FLASK_APP=app.py
export FLASK_DEBUG=1
export FN_FLASK_SECRET_KEY='flask-google-auth'

python -m flask run -p 8040