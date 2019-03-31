"""View Funcionários"""

from django.views.generic import TemplateView
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
#from django.contrib.auth.models import User
from .models import Funcionario, Fisioterapeuta, Administrador, Esteticista, Instrutor
from .forms import FuncionarioForm

class HomeView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView): # pylint: disable=too-many-ancestors,line-too-long
    """View da HomePage"""
    model = Funcionario
    template_name = "base.html"
    login_url = reverse_lazy('admin:login')
    permission_required = 'funcionarios.view_funcionario'

class FuncionarioView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView): # pylint: disable=too-many-ancestors,line-too-long
    """View da HomePage"""
    model = Funcionario
    template_name = "funcionarios/list.html"
    login_url = '/'
    login_url = reverse_lazy('admin:login')
    permission_required = 'funcionarios.view_funcionario'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['fisioterapeutas'] = Fisioterapeuta.objects.all()
        context['administradores'] = Administrador.objects.all()
        context['esteticistas'] = Esteticista.objects.all()
        context['instrutores'] = Instrutor.objects.all()
        return context

class AdministradorCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, View): # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Funcionarios Administradores"""
    template_name = 'funcionarios/administrador_form.html'
    success_message = "Administrador adicionado!"
    success_url = reverse_lazy('funcionarios:funcionario_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = {'funcionarios.add_funcionario', 'funcionarios.add_administrador'}

    def get(self, request, *args, **kwargs):
        """GET"""
        return render(request, self.template_name, {'form': FuncionarioForm})

    def post(self, request, *args, **kwargs):
        """POST"""
