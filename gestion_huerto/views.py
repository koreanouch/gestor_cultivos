# gestion_huerto/views.py
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cultivo, Sector

class CultivoListView(ListView):
    model = Cultivo
    template_name = "gestion_huerto/cultivo_lista.html"
    context_object_name = "cultivos"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["sectores"] = Sector.objects.annotate(total=Count("cultivos"))
        return ctx

class CultivoCreateView(CreateView):
    model = Cultivo
    fields = ["nombre", "fecha_siembra", "estado", "sector"]
    template_name = "gestion_huerto/cultivo_form.html"
    success_url = reverse_lazy("gestion_huerto:lista")

class CultivoUpdateView(UpdateView):
    model = Cultivo
    fields = ["nombre", "fecha_siembra", "estado", "sector"]
    template_name = "gestion_huerto/cultivo_form.html"
    success_url = reverse_lazy("gestion_huerto:lista")

class CultivoDeleteView(DeleteView):
    model = Cultivo
    template_name = "gestion_huerto/cultivo_confirmar_eliminar.html"
    success_url = reverse_lazy("gestion_huerto:lista")
