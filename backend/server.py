"""
The backend code for the am-i-covered app.

Run the server with `FLASK_APP=server.py flask run` (make sure your virtual environment
is activated).

Author:  Ian Fisher
Version: March 2019
"""
import json

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/api/events/<provider>")
def events(provider):
    """
    A JSON API endpoint for retrieving the appointment slots of the nurses who are
    covered by the given health insurance provider.
    """
    # TODO: sqlite3 instead of JSON?
    with open("data.json", "r") as f:
        data = json.load(f)

    response = jsonify(data.get(provider, []))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
