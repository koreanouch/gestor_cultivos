# gestion_huerto/admin.py
from django.contrib import admin
from .models import Sector, Cultivo

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

@admin.register(Cultivo)
class CultivoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_siembra", "estado", "sector")
    list_filter = ("estado", "sector")
    search_fields = ("nombre",)
