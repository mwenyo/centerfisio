"""Endereçamento de Pacientes"""

from django.urls import path
from .views import PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView

app_name = 'pacientes'

urlpatterns = [
    path('', PacienteListView.as_view(), name="paciente_list"),
    path('adicionar', PacienteCreateView.as_view(),
         name="paciente_adicionar"),
    path('<int:pk>/editar',
         PacienteUpdateView.as_view(), name="paciente_editar"),
    path('<int:pk>/deletar',
         PacienteDeleteView.as_view(), name="paciente_deletar"),

]
