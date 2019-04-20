"""URLs Clinica"""
from django.urls import path
from .views import ConvenioView, ConvenioUpdateView, ConvenioCreateView, ConvenioDeleteView
from .views import ProcedimentoView, ProcedimentoCreateView
from .views import ProcedimentoUpdateView, ProcedimentoDeleteView
from .views import PacoteView, PacoteCreateView, PacoteDeleteView
from .views import PacoteUpdateView, PacoteDetailView
from .views import PacoteProcedimentoDeleteView, PacoteProcedimentoCreateView

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

    path('pacotes/', PacoteView.as_view(), name="pacote_lista"),
    path('pacotes/adicionar', PacoteCreateView.as_view(),
         name="pacote_adicionar"),
    path('pacotes/<int:pk>/editar',
         PacoteUpdateView.as_view(), name="pacote_editar"),
    path('pacotes/<int:pk>/deletar',
         PacoteDeleteView.as_view(), name="pacote_deletar"),
    path('pacotes/<int:pk>/procedimento_deletar',
         PacoteProcedimentoDeleteView.as_view(), name="pacote_procedimento_deletar"),
    path('pacotes/<int:pk>/procedimento_adicionar',
         PacoteProcedimentoCreateView.as_view(), name="pacote_procedimento_adicionar"),
    path('pacotes/<int:pk>/detalhes',
         PacoteDetailView.as_view(), name="pacote_detalhes"),
]
