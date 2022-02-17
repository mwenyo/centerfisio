from django.urls import path
from .views import FormaDePagamentoListView
from .views import FormaDePagamentoListAjaxView
from .views import FormaDePagamentoDeleteView
from .views import FormaDePagamentoUpdateView
from .views import FormaDePagamentoCreateView

from .views import CaixaListView
from .views import CaixaDetailView
from .views import CaixaAbrirView
from .views import CaixaFecharView
from .views import CaixaMovimentacaoView
from .views import CaixaUltimoAbertoAjaxView
from .views import CaixaReceberAjaxView

from .views import AgendamentoCreateView
from .views import AgendamentoListView
from .views import AgendamentosAjaxListView
from .views import AgendamentoAjaxDetailView
from .views import AgendamentoAjaxEditView
from .views import AgendamentoAjaxDeleteView

from .views import MovimentacaoCreateView
from .views import MovimentacaoUpdateView
from .views import MovimentacaoDeleteView

from .views import UsuarioAjaxListView

app_name = 'movimentacoes'

urlpatterns = [
    # FORMAS DE PAGAMENTO
    path('formas_de_pagamento/',
         FormaDePagamentoListView.as_view(),
         name="forma_de_pagamento_list"),

    path('formas_de_pagamento_ajax/',
         FormaDePagamentoListAjaxView.as_view(),
         name="forma_de_pagamento_list_ajax"),

    path('forma_pgto/<str:id>/excluir/',
         FormaDePagamentoDeleteView.as_view(),
         name="forma_de_pagamento_delete"),

    path('forma_pgto/<str:id>/editar/',
         FormaDePagamentoUpdateView.as_view(),
         name="forma_de_pagamento_edit"),

    path('forma_pgto/adicionar/',
         FormaDePagamentoCreateView.as_view(),
         name="forma_de_pagamento_create"),

    # CAIXA
    path('caixas/',
         CaixaListView.as_view(),
         name="caixa_list"),

    path('caixa/movimentacao/',
         CaixaMovimentacaoView.as_view(),
         name="caixa_movimentacao"),

    path('caixa/<str:pk>/detalhes/',
         CaixaDetailView.as_view(),
         name="caixa_detail"),

    path('caixa/<str:id>/fechar/',
         CaixaFecharView.as_view(),
         name="caixa_fechar"),

    path('caixa/receber/<str:id>/',
         CaixaReceberAjaxView.as_view(),
         name="caixa_receber"),

    path('caixa/adicionar/',
         CaixaAbrirView.as_view(),
         name="caixa_abrir"),

    path('caixa/aberto_ajax/',
         CaixaUltimoAbertoAjaxView.as_view(),
         name="caixa_aberto"),

    # AGENDAMENTOS

    path('agendamentos/',
         AgendamentoListView.as_view(),
         name="agendamento_list"),

    path('agendamentos/adicionar/',
         AgendamentoCreateView.as_view(),
         name="agendamento_create"),

    path('agendamentos/lista_ajax/',
         AgendamentosAjaxListView.as_view(),
         name="agendamento_list_ajax"),

    path('agendamentos/detalhe_ajax/<str:id>/',
         AgendamentoAjaxDetailView.as_view(),
         name="agendamento_detail_ajax"),

    path('agendamentos/editar_ajax/<str:id>/',
         AgendamentoAjaxEditView.as_view(),
         name="agendamento_edit_ajax"),

    path('agendamentos/excluir_ajax/<str:id>/',
         AgendamentoAjaxDeleteView.as_view(),
         name="agendamento_delete_ajax"),

    # PROFISSIONAIS

    path('usuarios/buscar_profissionais/',
         UsuarioAjaxListView.as_view(),
         name="agendamento_lista_ajax"),

    # MOVIMENTAÇÕES
    path('movimentacao/<str:id>/excluir/',
         MovimentacaoDeleteView.as_view(),
         name="movimentacao_delete"),

    path('movimentacao/adicionar/',
         MovimentacaoCreateView.as_view(),
         name="movimentacao_create"),

    path('movimentacao/<str:id>/editar/',
         MovimentacaoUpdateView.as_view(),
         name="movimentacao_edit"),
]
