"""
Populate the database with sample nurses and appointment slots.

Run with your virtual environment activated:

  python3 populate_db.py


Author:  Ian Fisher (iafisher@protonmail.com)
Version: May 2019
"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hccoverage.settings")
import django
django.setup()

import datetime
from coverage_app.models import Appointment, Nurse, Provider


# Delete everything in the database.
Nurse.objects.all().delete()
Provider.objects.all().delete()
Appointment.objects.all().delete()

anna = Nurse.objects.create(name="Anna")
richard = Nurse.objects.create(name="Richard")
yasmine = Nurse.objects.create(name="Yasmine")

aetna = Provider.objects.create(name="aetna")
bcbs = Provider.objects.create(name="bcbs")
humana = Provider.objects.create(name="humana")
kp = Provider.objects.create(name="kp")

aetna.nurses.add(richard, yasmine)
bcbs.nurses.add(anna, yasmine)
humana.nurses.add(anna, richard)
kp.nurses.add(yasmine)

# Create appointments for every week in 2019, starting the week of March 18.
monday = datetime.date(2019, 3, 18)
while monday.year == 2019:
    tuesday = monday + datetime.timedelta(1)
    wednesday = monday + datetime.timedelta(2)
    thursday = monday + datetime.timedelta(3)
    friday = monday + datetime.timedelta(4)

    Appointment.objects.create(date=monday.isoformat(), start=600, end=660, nurse=anna)
    Appointment.objects.create(date=wednesday.isoformat(), start=600, end=660, nurse=anna)
    Appointment.objects.create(date=friday.isoformat(), start=600, end=660, nurse=anna)

    Appointment.objects.create(date=tuesday.isoformat(), start=900, end=930, nurse=richard)
    Appointment.objects.create(date=thursday.isoformat(), start=900, end=930, nurse=richard)

    Appointment.objects.create(date=monday.isoformat(), start=720, end=765, nurse=yasmine)
    Appointment.objects.create(date=wednesday.isoformat(), start=720, end=765, nurse=yasmine)
    Appointment.objects.create(date=friday.isoformat(), start=720, end=765, nurse=yasmine)

    monday = monday + datetime.timedelta(7)
