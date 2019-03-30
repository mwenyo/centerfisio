"""Endereçamento de Funcionários"""

from django.urls import path
from .views import HomeView, FuncionarioCreateView, FuncionarioView

app_name = 'funcionarios'

urlpatterns = [
    path('', HomeView.as_view(), name="pagina_inicial"),
    path('funcionarios/', FuncionarioView.as_view(), name="funcionario_lista"),
    path('funcionarios/adicionar', FuncionarioCreateView.as_view(), \
        name="funcionarios_adicionar"),
]
