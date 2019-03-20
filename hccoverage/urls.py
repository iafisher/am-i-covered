from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("demos/am-i-covered/", include("coverage_app.urls")),
]
