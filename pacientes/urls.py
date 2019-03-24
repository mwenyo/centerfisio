"""Endereçamento de Pacientes"""

from django.urls import path
from .views import PacienteListView

app_name = 'pacientes'

urlpatterns = [
    path('', PacienteListView.as_view(), name="paciente_list"),
]
