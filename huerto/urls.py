# proyecto_huerto/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("gestion_huerto.urls")),  # namespace proviene de app_name
]