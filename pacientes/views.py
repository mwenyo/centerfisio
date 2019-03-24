"""View do App Paciente"""
#from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView

from .models import Paciente

@method_decorator(login_required, name='dispatch')
class PacienteListView(ListView):
    """ListView Pacientes"""
    model = Paciente
    template_name = 'pacientes/list.html'
