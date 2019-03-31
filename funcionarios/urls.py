"""Endereçamento de Funcionários"""

from django.urls import path
from .views import HomeView, AdministradorCreateView, FuncionarioView

app_name = 'funcionarios'

urlpatterns = [
    path('', HomeView.as_view(), name="pagina_inicial"),
    path('funcionarios/', FuncionarioView.as_view(), name="funcionario_lista"),
    path('funcionarios/admin/adicionar', AdministradorCreateView.as_view(), \
        name="funcionarios_admin_adicionar"),
]
