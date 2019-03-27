import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hccoverage.settings")
import django
django.setup()

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


Appointment.objects.create(date="2019-03-18", start=600, end=660, nurse=anna)
Appointment.objects.create(date="2019-03-20", start=600, end=660, nurse=anna)
Appointment.objects.create(date="2019-03-22", start=600, end=660, nurse=anna)

Appointment.objects.create(date="2019-03-19", start=900, end=930, nurse=richard)
Appointment.objects.create(date="2019-03-21", start=900, end=930, nurse=richard)

Appointment.objects.create(date="2019-03-18", start=720, end=765, nurse=yasmine)
Appointment.objects.create(date="2019-03-20", start=720, end=765, nurse=yasmine)
Appointment.objects.create(date="2019-03-22", start=720, end=765, nurse=yasmine)

Appointment.objects.create(date="2019-03-25", start=600, end=660, nurse=anna)
Appointment.objects.create(date="2019-03-27", start=600, end=660, nurse=anna)
Appointment.objects.create(date="2019-03-29", start=600, end=660, nurse=anna)

Appointment.objects.create(date="2019-03-26", start=900, end=930, nurse=richard)
Appointment.objects.create(date="2019-03-28", start=900, end=930, nurse=richard)

Appointment.objects.create(date="2019-03-25", start=720, end=765, nurse=yasmine)
Appointment.objects.create(date="2019-03-27", start=720, end=765, nurse=yasmine)
Appointment.objects.create(date="2019-03-29", start=720, end=765, nurse=yasmine)
