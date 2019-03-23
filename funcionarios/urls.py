"""Endereçamento de Funcionários"""

from django.urls import path
from .views import HomeView

app_name = 'funcionarios'

urlpatterns = [
    path('', HomeView.as_view(), name="pagina_inicial"),
]
