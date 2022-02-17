from django.urls import path

from .views import ProcedimentoListView
from .views import ProcedimentoCreateView
from .views import ProcedimentoUpdateView
from .views import ProcedimentoDeleteView
from .views import ProcedimentoAjaxListView
from .views import ProcedimentoAjaxListView2

from .views import PromocaoListView
from .views import PromocaoDetailView
from .views import PromocaoCreateView
from .views import PromocaoUpdateView
from .views import PromocaoDeleteView

from .views import ProcedimentoPromocaoCreateView
from .views import ProcedimentoPromocaoUpdateView
from .views import ProcedimentoPromocaoDeleteView
from .views import ProcedimentoPromocaoAjaxListView

app_name = 'procedimentos'

urlpatterns = [

    # PROCEDIMENTOS
    path('procedimentos', ProcedimentoListView.as_view(),
         name='procedimento_list'),
    path('procedimentos/adicionar/', ProcedimentoCreateView.as_view(),
         name='procedimento_create'),
    path('procedimentos/<str:id>/editar/', ProcedimentoUpdateView.as_view(),
         name='procedimento_edit'),
    path('procedimentos/<str:id>/excluir/', ProcedimentoDeleteView.as_view(),
         name='procedimento_delete'),

    path('procedimentos/<str:id>/listar/',
         ProcedimentoAjaxListView.as_view(),
         name='procedimento_ajax_list'),
    path('procedimentos/buscar_procedimentos/',
         ProcedimentoAjaxListView2.as_view(),
         name='procedimento_ajax_list2'),

    # PROMOÇÕES
    path('promocoes', PromocaoListView.as_view(),
         name='promocao_list'),
    path('promocoes/<str:pk>/detalhes/', PromocaoDetailView.as_view(),
         name='promocao_detail'),
    path('promocoes/adicionar/', PromocaoCreateView.as_view(),
         name='promocao_create'),
    path('promocoes/<str:id>/editar/', PromocaoUpdateView.as_view(),
         name='promocao_edit'),
    path('promocoes/<str:id>/excluir/', PromocaoDeleteView.as_view(),
         name='promocao_delete'),

    # PROCEDIMENTOS EM PROMOÇÃO
    path('procedimentos_promocoes/adicionar/',
         ProcedimentoPromocaoCreateView.as_view(),
         name='procedimento_promocao_create'),

    path('procedimentos_promocoes/<str:id>/editar/',
         ProcedimentoPromocaoUpdateView.as_view(),
         name='procedimento_promocao_edit'),

    path('procedimentos_promocoes/<str:id>/excluir/',
         ProcedimentoPromocaoDeleteView.as_view(),
         name='procedimento_promocao_delete'),

    path('procedimentos_promocoes/buscar_procedimentos/',
         ProcedimentoPromocaoAjaxListView.as_view(),
         name='procedimento_ajax_list2'),
]
