"""View Funcionários"""

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
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

class AdministradorCreateView(LoginRequiredMixin, PermissionRequiredMixin, View): # pylint: disable=too-many-ancestors,line-too-long
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
        form = FuncionarioForm(request.POST, request.FILES or None)
        if form.is_valid():
            clean = form.cleaned_data
            usuario = User(
                username=clean['nome_usuario'],
                first_name=clean['nome'],
                last_name=clean['sobrenome'],
                password='vai mudar',
                email=clean['email'],
                is_staff=True,
            )
            usuario.set_password(clean['senha'])
            usuario.save()

            funcionario = Funcionario(
                usuario=usuario,
                cpf=clean['cpf'],
                nascimento=clean['nascimento'],
                contratacao=clean['contratacao'],
                telefone1=clean['telefone1'],
                telefone2=clean['telefone2'],
                endereco=clean['endereco'],
                complemento=clean['complemento'],
                numero=clean['numero'],
                bairro=clean['bairro'],
                cidade=clean['cidade'],
                uf=clean['uf'],
                estado_civil=clean['estado_civil'],
                genero=clean['genero'],
                foto=request.FILES['foto'],
            )

            funcionario.save()

            adm = Administrador(funcionario=funcionario)
            adm.save()

            messages.success(request,
                             'Administrador %s adicionado com sucesso!' \
                                 % adm.funcionario.nome_completo)

            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})
