from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("demos/am-i-covered/admin/", admin.site.urls),
    path("demos/am-i-covered/", include("coverage_app.urls")),
]
