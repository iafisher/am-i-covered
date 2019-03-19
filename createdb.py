"""
Create the database and fill it with some placeholder data.

Author:  Ian Fisher (iafisher@protonmail.com)
Version: March 2019
"""
import os
import sqlite3
import sys


# If you change the name of the database here, you'll also have to change it in
# server.py.
DATABASE = "db.sqlite3"


if os.path.exists(DATABASE):
    yesno = input(
        "Database already exists. Do you wish to destroy it and make a new one? "
    )
    if yesno.lower().startswith("y"):
        print("\nCreating new database.")
        os.remove(DATABASE)
    else:
        print("\nExiting.")
        sys.exit(0)


with sqlite3.connect("db.sqlite3") as conn:
    conn.executescript(
        """
        -- Create the Nurses table.
        CREATE TABLE Nurses (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255),
            providers VARCHAR(1024)  -- A comma-separated list
        );

        -- Create the "Appointments" table.
        CREATE TABLE Appointments (
            id INTEGER PRIMARY KEY,
            date VARCHAR(12),
            start INTEGER,  -- As minutes since midnight
            end INTEGER,
            nurse_id INTEGER NOT NULL,
            FOREIGN KEY (nurse_id) REFERENCES Nurses(id)
        );

        -- Populate the tables with data.
        INSERT INTO Nurses (name, providers)
        VALUES ('Anna', 'bcbs,kp');

        INSERT INTO Nurses (name, providers)
        VALUES ('Richard', 'humana,aetna');

        INSERT INTO Nurses (name, providers)
        VALUES ('Yasmine', 'kp,bcbs,aetna');

        INSERT INTO Appointments (date, start, end, nurse_id)
        VALUES (
            "2019-03-18",
            -- 10:00 to 11:00
            600,
            660, 
            (SELECT id FROM Nurses WHERE name = 'Anna')
        );

        INSERT INTO Appointments (date, start, end, nurse_id)
        VALUES (
            "2019-03-20",
            -- 10:00 to 11:00
            600,
            660, 
            (SELECT id FROM Nurses WHERE name = 'Anna')
        );

        INSERT INTO Appointments (date, start, end, nurse_id)
        VALUES (
            "2019-03-22",
            -- 10:00 to 11:00
            600,
            660, 
            (SELECT id FROM Nurses WHERE name = 'Anna')
        );

        INSERT INTO Appointments (date, start, end, nurse_id)
        VALUES (
            "2019-03-19",
            -- 3:00 to 3:30
            900,
            930, 
            (SELECT id FROM Nurses WHERE name = 'Richard')
        );

        INSERT INTO Appointments (date, start, end, nurse_id)
        VALUES (
            "2019-03-21",
            -- 3:00 to 3:30
            900,
            930, 
            (SELECT id FROM Nurses WHERE name = 'Richard')
        );

        INSERT INTO Appointments (date, start, end, nurse_id)
        VALUES (
            "2019-03-18",
            -- 12:00 to 12:45
            720,
            765, 
            (SELECT id FROM Nurses WHERE name = 'Yasmine')
        );

        INSERT INTO Appointments (date, start, end, nurse_id)
        VALUES (
            "2019-03-20",
            -- 12:00 to 12:45
            720,
            765, 
            (SELECT id FROM Nurses WHERE name = 'Yasmine')
        );

        INSERT INTO Appointments (date, start, end, nurse_id)
        VALUES (
            "2019-03-22",
            -- 12:00 to 12:45
            720,
            765, 
            (SELECT id FROM Nurses WHERE name = 'Yasmine')
        );
        """
    )
