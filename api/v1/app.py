#!/usr/bin/python3
''' module that makes this an app '''

from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close():
    ''' method that close the yes '''
    storage.close()

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST")
    if not host:
        host = "0.0.0.0"
    port = getenv("HBNB_API_PORT")
    if not port:
        port = "5000"
    app.run(host=host, port=port, threaded=True)
