import os
import subprocess
from functools import wraps

from flask import request, jsonify, Flask

KODI_PROCESS = "kodi"
# local test
# KODI_PROCESS = "ntp"


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return jsonify({'message': 'token is missing'})
        if token != os.environ.get('TOKEN'):
            return jsonify({'message': 'invalid token'})

        return f(*args, **kwargs)

    return decorator


def create_app():
    app = Flask(__name__)
    app.config.update({
        "TOKEN": os.environ.get("TOKEN")
    })

    @app.route('/')
    @token_required
    def index():
        return {"APP": "ok"}

    @app.route('/kodi/restart/', methods=('GET', 'POST'))
    @token_required
    def kodi_restart():
        if request.method == 'POST':
            print("Starting Kodi")
            command = f"sudo systemctl restart {KODI_PROCESS}"
            print("execute command: %s" % command)
            child = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            # wait for the command result
            child.communicate()
            rc = child.returncode
            return {"code": rc}
        return {"kodi": "restart"}

    return app


app = create_app()








