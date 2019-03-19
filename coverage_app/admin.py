from django.contrib import admin

from .models import Appointment, Nurse, Provider


admin.site.register(Appointment)
admin.site.register(Nurse)
admin.site.register(Provider)
