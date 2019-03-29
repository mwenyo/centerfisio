"""URLs Clinica"""
from django.urls import path
from .views import ConvenioView, ConvenioUpdateView, ConvenioCreateView, ConvenioDeleteView
from .views import ProcedimentoView, ProcedimentoCreateView, \
    ProcedimentoUpdateView, ProcedimentoDeleteView

app_name = 'clinica'

urlpatterns = [
    path('convenios/', ConvenioView.as_view(), name="convenio_lista"),
    path('convenios/adicionar', ConvenioCreateView.as_view(), name="convenio_adicionar"),
    path('convenios/<int:pk>/editar', ConvenioUpdateView.as_view(), name="convenio_editar"),
    path('convenios/<int:pk>/deletar', ConvenioDeleteView.as_view(), name="convenio_deletar"),

    path('procedimentos/', ProcedimentoView.as_view(), name="procedimento_lista"),
    path('procedimentos/adicionar', ProcedimentoCreateView.as_view(), \
        name="procedimento_adicionar"),
    path('procedimentos/<int:pk>/editar', ProcedimentoUpdateView.as_view(), \
        name="procedimento_editar"),
    path('procedimentos/<int:pk>/deletar', ProcedimentoDeleteView.as_view(), \
        name="procedimento_deletar"),
]
