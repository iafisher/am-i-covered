from django.urls import path

from . import views


app_name = "coverage_app"


urlpatterns = [
    path("", views.index, name="index"),
    path("appointment", views.appointment, name="appointment"),
    path("api/events/<provider>", views.events_api, name="events_api"),
]
