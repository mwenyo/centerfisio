"""Endereçamento de Funcionários"""

from django.urls import path
from . import views

app_name = 'funcionarios'

urlpatterns = [
    path('', views.home, name="pagina_inicial"),
]
