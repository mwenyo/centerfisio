from django.urls import path

from .views import PacienteListView
from .views import PacienteCreateView
from .views import PacienteUpdateView
from .views import PacienteDeleteView
from .views import PacienteDetailView
from .views import PacienteListAjaxView
from .views import PacienteCreateAjaxView

app_name = 'pacientes'

urlpatterns = [
    path('', PacienteListView.as_view(), name="paciente_list"),
    path('adicionar/', PacienteCreateView.as_view(), name="paciente_add"),
    path('adicionar/ajax/', PacienteCreateAjaxView.as_view(),
         name="paciente_add_ajax"),
    path('buscar_pacientes/', PacienteListAjaxView.as_view(),
         name="paciente_buscar"),
    path('<int:pk>/editar/', PacienteUpdateView.as_view(),
         name="paciente_edit"),
    path('<int:pk>/excluir/', PacienteDeleteView.as_view(),
         name="paciente_delete"),
    path('<int:pk>/detalhes/', PacienteDetailView.as_view(),
         name="paciente_detail"),
]
