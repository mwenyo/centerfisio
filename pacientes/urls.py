"""Endereçamento de Pacientes"""

from django.urls import path
from .views import PacienteListView
from .views import PacienteCreateView
from .views import PacienteUpdateView
from .views import PacienteDeleteView
from .views import PacienteDetailView

app_name = 'pacientes'

urlpatterns = [
    path('', PacienteListView.as_view(), name="paciente_list"),
    path('<int:pk>/detalhes',
         PacienteDetailView.as_view(), name="paciente_detalhes"),
    path('adicionar', PacienteCreateView.as_view(),
         name="paciente_adicionar"),
    path('<int:pk>/editar',
         PacienteUpdateView.as_view(), name="paciente_editar"),
    path('<int:pk>/deletar',
         PacienteDeleteView.as_view(), name="paciente_deletar"),

]
