# gestion_huerto/urls.py
from django.urls import path
from .views import (
    CultivoListView, CultivoCreateView,
    CultivoUpdateView, CultivoDeleteView
)

app_name = "gestion_huerto"

urlpatterns = [
    path("", CultivoListView.as_view(), name="lista"),
    path("nuevo/", CultivoCreateView.as_view(), name="crear"),
    path("<int:pk>/editar/", CultivoUpdateView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", CultivoDeleteView.as_view(), name="eliminar"),
]
