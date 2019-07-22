# Flask-Google-Auth
Demo App : Google Authentication (Login) implemented in the typical Flask App

## Instructions
Follow these instructions to run this:
*   Create the **GOGOLE_AUTH_CLIENT_ID** from the GCP console
*   Create the **GOGOLE_AUTH_SECRET_ID** from the GCP console
*   Store those credentials either in system env or in run.sh
    *   If you are storing them as environment variables. modify the code of run.sh to access them from env
*   After, modifying the run.sh. We need to make run.sh executable:
    *   Command: `chmod +x run.sh`
    *   Run: `./run`

Go to browser and open: `http://localhost:8040`

For login using google auth: redirect to `http://localhost:8040/google/login`. It will open google auth page.

For logout , redirect to `http://localhost:8040/google/logout`

## Note:
Do not change the port, The redirect url is used for generating the auth credentials If you changed it, u will not be able to run it.

For using in production, Generate a new **OAuthClientId** credentials with the **Domain verfication** and proper authorise URL.