from django.http import JsonResponse
from django.shortcuts import render

from .models import Appointment, Nurse, Provider


def index(request):
    return render(request, "coverage_app/index.html")


def appointment(request):
    return render(request, "coverage_app/appointment.html")


def events_api(request, provider):
    provider_object = Provider.objects.get(name=provider)
    nurses = Nurse.objects.filter(provider=provider_object)
    appointments = []
    for nurse in nurses:
        appointments.extend(list(Appointment.objects.filter(nurse=nurse)))

    data = []
    for aptmt in appointments:
        data.append({
            "title": str(aptmt.nurse),
            "start": aptmt.date + "T" + minutes_to_hours(aptmt.start),
            "end": aptmt.date + "T" + minutes_to_hours(aptmt.end),
        })
    return JsonResponse(data, safe=False)


def minutes_to_hours(minutes):
    return "{}:{:0>2}".format(*divmod(minutes, 60))
