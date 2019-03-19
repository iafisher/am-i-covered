"""
The backend code for the am-i-covered app.

Run the server with `FLASK_APP=server.py flask run` (make sure your virtual environment
is activated). You'll also need to run `python3 createdb.py` beforehand so that the
database exists.

Author:  Ian Fisher
Version: March 2019
"""
import json
import sqlite3

from flask import Flask, g, jsonify, render_template


app = Flask(__name__)
# If you change the name of the database here, you'll also have to change it in
# createdb.py.
DATABASE = "db.sqlite3"


@app.route("/")
def index_view():
    return render_template("index.html")


@app.route("/appointment")
def appointments_view():
    return render_template("appointment.html")


@app.route("/api/events/<provider>")
def events(provider):
    """
    A JSON API endpoint for retrieving the appointment slots of the nurses who are
    covered by the given health insurance provider.
    """
    data = get_data_db(provider)
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


def get_data_db(provider):
    rows = query_db("""
        SELECT 
            Nurses.name, Appointments.date, Appointments.start, Appointments.end
        FROM 
            Appointments
        INNER JOIN
            Nurses ON Appointments.nurse_id = Nurses.id
        WHERE
            Nurses.providers LIKE ?
        ;
    """, ("%" + provider + "%",))

    data = []
    for row in rows:
        data.append({
            "title": "Nurse " + row["name"],
            "start": row["date"] + "T" + minutes_to_hours(row["start"]),
            "end": row["date"] + "T" + minutes_to_hours(row["end"]),
        })
    return data


def get_data_json(provider):
    with open("data.json", "r") as f:
        data = json.load(f)
    return data.get(provider, [])


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.teardown_appcontext
def close_connection(exception):
    # Make sure the database connection is closed when the server shuts down.
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def minutes_to_hours(minutes):
    return "{}:{:0>2}".format(*divmod(minutes, 60))
