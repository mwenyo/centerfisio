"""Endereçamento de Funcionários"""

from django.urls import path
from .views import HomeView, FuncionarioView, FuncionarioDeleteView
from .views import AdministradorCreateView, AdministradorUpdateView
from .views import FisioterapeutaCreateView, FisioterapeutaUpdateView
from .views import EsteticistaCreateView, EsteticistaUpdateView
from .views import InstrutorCreateView, InstrutorUpdateView

app_name = 'funcionarios'

urlpatterns = [
    path('', HomeView.as_view(), name="pagina_inicial"),
    path('funcionarios/', FuncionarioView.as_view(), name="funcionario_lista"),
    path('funcionarios/<int:pk>/deletar', FuncionarioDeleteView.as_view(), \
        name="funcionario_deletar"),

    path('funcionarios/administradores/adicionar', AdministradorCreateView.as_view(),\
         name="funcionario_admin_adicionar"),
    path('funcionarios/administradores/<int:pk>/editar', AdministradorUpdateView.as_view(), \
        name="funcionario_admin_editar"),

    path('funcionarios/fisioterapeutas/adicionar', FisioterapeutaCreateView.as_view(),\
         name="funcionario_fisio_adicionar"),
    path('funcionarios/fisioterapeutas/<int:pk>/editar', FisioterapeutaUpdateView.as_view(), \
        name="funcionario_fisio_editar"),

    path('funcionarios/esteticistas/adicionar', EsteticistaCreateView.as_view(),\
            name="funcionario_estet_adicionar"),
    path('funcionarios/esteticistas/<int:pk>/editar', EsteticistaUpdateView.as_view(), \
        name="funcionario_estet_editar"),

    path('funcionarios/instrutores/adicionar', InstrutorCreateView.as_view(),\
            name="funcionario_intru_adicionar"),
    path('funcionarios/instrutores/<int:pk>/editar', InstrutorUpdateView.as_view(), \
        name="funcionario_intru_editar")
]