"""View Funcionários"""

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Funcionario, Fisioterapeuta, Administrador, Esteticista, Instrutor

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

class FuncionarioCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView): # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Funcionarios"""
    model = Funcionario
    fields = ['nome', 'status']
    template_name = "clinica/convenio/form.html"
    success_message = "Convênio adicionado!"
    success_url = reverse_lazy('clinica:convenio_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.add_convenio'
