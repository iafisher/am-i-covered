"""
The backend code for the am-i-covered app.

Run the server with `FLASK_APP=server.py flask run` (make sure your virtual environment
is activated).

Author:  Ian Fisher
Version: February 2019
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/api/events/<provider>")
def events(provider):
    # Just return some hard-coded data for now.
    response = jsonify([{"title": "Nurse Anna", "start": "2019-03-04", "end": "2019-03-04"}])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
