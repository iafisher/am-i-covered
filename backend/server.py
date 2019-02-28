"""
The backend code for the am-i-covered app.

Run with

$ FLASK_APP=server.py flask run

(Make sure your virtual environment is activated.)

Author:  Ian Fisher
Version: February 2019
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, world"

@app.route("/api/events")
def events():
    response = jsonify([{"nurse": "Nurse Anna", "date": "2019-03-04"}])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
