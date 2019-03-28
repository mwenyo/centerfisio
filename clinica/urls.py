"""URLs Clinica"""
from django.urls import path
from .views import ConvenioView, ConvenioUpdateView, ConvenioCreateView, ConvenioDeleteView

app_name = 'clinica'

urlpatterns = [
    path('convenios/', ConvenioView.as_view(), name="convenio_lista"),
    path('convenios/adicionar', ConvenioCreateView.as_view(), name="convenio_adicionar"),
    path('convenios/<int:pk>/editar', ConvenioUpdateView.as_view(), name="convenio_editar"),
    path('convenios/<int:pk>/deletar', ConvenioDeleteView.as_view(), name="convenio_deletar"),
]
