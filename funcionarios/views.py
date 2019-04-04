"""View Funcionários"""

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Funcionario, Fisioterapeuta, Administrador, Esteticista, Instrutor
from .forms import FuncionarioCreateForm, FuncionarioUpdateForm
from .forms import FisioterapeutaCreateForm, FisioterapeutaUpdateForm
from .forms import EsteticistaCreateForm, EsteticistaUpdateForm
from .forms import InstrutorCreateForm, InstrutorUpdateForm


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

class FuncionarioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView): # pylint: disable=too-many-ancestors,line-too-long
    """Excluir Usuários"""
    model = User
    template_name = 'funcionarios/delete.html'
    success_message = "Funcionario excluído!"
    success_url = reverse_lazy('funcionarios:funcionario_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'funcionarios.delete_funcionario'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(FuncionarioDeleteView, self).delete(request, *args, **kwargs)

class AdministradorCreateView(LoginRequiredMixin, PermissionRequiredMixin, View): # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Funcionarios Administradores"""
    template_name = 'funcionarios/administrador_form.html'
    success_message = "Administrador adicionado!"
    success_url = reverse_lazy('funcionarios:funcionario_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = {'funcionarios.add_funcionario',
                           'funcionarios.add_administrador'}

    def get(self, request, *args, **kwargs):
        """GET"""
        return render(request, self.template_name, {'form': FuncionarioCreateForm})

    def post(self, request, *args, **kwargs):
        """POST"""
        form = FuncionarioCreateForm(request.POST, request.FILES or None)
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

class AdministradorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View): # pylint: disable=too-many-ancestors,line-too-long
    """Editar Funcionarios Administradores"""
    template_name = 'funcionarios/administrador_form.html'
    success_message = "Dados atualizados!"
    success_url = reverse_lazy('funcionarios:funcionario_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = {'funcionarios.change_funcionario',
                           'funcionarios.change_administrador'}

    def get(self, request, *args, **kwargs):
        """GET"""
        admin = Administrador.objects.get(id=kwargs['pk'])
        dados = {
            'nome_usuario': admin.funcionario.usuario.username,
            'email': admin.funcionario.usuario.email,
            'nome': admin.funcionario.usuario.first_name,
            'sobrenome': admin.funcionario.usuario.last_name,
            'cpf': admin.funcionario.cpf,
            'nascimento': admin.funcionario.nascimento,
            'contratacao': admin.funcionario.contratacao,
            'telefone1': admin.funcionario.telefone1,
            'telefone2': admin.funcionario.telefone2,
            'endereco': admin.funcionario.endereco,
            'complemento': admin.funcionario.complemento,
            'numero': admin.funcionario.numero,
            'bairro': admin.funcionario.bairro,
            'cidade': admin.funcionario.cidade,
            'uf': admin.funcionario.uf,
            'estado_civil': admin.funcionario.estado_civil,
            'genero': admin.funcionario.genero,
        }
        context = {
            'object': admin,
            'form': FuncionarioUpdateForm(initial=dados)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """POST"""
        admin = Administrador.objects.get(id=kwargs['pk'])
        form = FuncionarioUpdateForm(request.POST or None)
        if form.is_valid():

            clean = form.cleaned_data

            admin.funcionario.usuario.username = clean['nome_usuario']
            admin.funcionario.usuario.first_name = clean['nome']
            admin.funcionario.usuario.last_name = clean['sobrenome']
            admin.funcionario.usuario.email = clean['email']

            admin.funcionario.usuario.save(update_fields=[
                'username', 'first_name', 'last_name', 'email',
            ])

            admin.funcionario.cpf = clean['cpf']
            admin.funcionario.nascimento = clean['nascimento']
            admin.funcionario.contratacao = clean['contratacao']
            admin.funcionario.telefone1 = clean['telefone1']
            admin.funcionario.telefone2 = clean['telefone2']
            admin.funcionario.endereco = clean['endereco']
            admin.funcionario.complemento = clean['complemento']
            admin.funcionario.numero = clean['numero']
            admin.funcionario.bairro = clean['bairro']
            admin.funcionario.cidade = clean['cidade']
            admin.funcionario.uf = clean['uf']
            admin.funcionario.estado_civil = clean['estado_civil']
            admin.funcionario.genero = clean['genero']

            admin.funcionario.save(update_fields=[
                'cpf', 'nascimento', 'contratacao', 'telefone1', 'telefone2',
                'endereco', 'complemento', 'numero', 'bairro', 'cidade',
                'uf', 'estado_civil', 'genero',
            ])

            admin.funcionario.save()

            messages.success(request, 'Dados alterados com sucesso!')

            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})

class FisioterapeutaCreateView(LoginRequiredMixin, PermissionRequiredMixin, View): # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Funcionarios Fisioterapeutas"""
    template_name = 'funcionarios/fisioterapeuta_form.html'
    success_message = "Fisioterapeuta adicionado!"
    success_url = reverse_lazy('funcionarios:funcionario_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = {'funcionarios.add_funcionario',
                           'funcionarios.add_fisioterapeuta'}

    def get(self, request, *args, **kwargs):
        """GET"""
        return render(request, self.template_name, {'form': FisioterapeutaCreateForm})

    def post(self, request, *args, **kwargs):
        """POST"""
        form = FisioterapeutaCreateForm(request.POST, request.FILES or None)
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

            fisio = Fisioterapeuta(
                funcionario=funcionario,
                crefito=clean['crefito'],
                especializacao=clean['especializacao'],
                cursos=clean['cursos']
                )
            fisio.save()

            messages.success(request,
                             'Fisioterapeuta %s adicionado com sucesso!' \
                                 % fisio.funcionario.nome_completo)

            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})

class FisioterapeutaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View): # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Funcionarios Fisioterapeutas"""
    template_name = 'funcionarios/fisioterapeuta_form.html'
    success_message = "Fisioterapeuta adicionado!"
    success_url = reverse_lazy('funcionarios:funcionario_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = {'funcionarios.change_funcionario',
                           'funcionarios.change_fisioterapeuta'}

    def get(self, request, *args, **kwargs):
        """GET"""
        fisio = Fisioterapeuta.objects.get(id=kwargs['pk'])
        dados = {
            'nome_usuario': fisio.funcionario.usuario.username,
            'email': fisio.funcionario.usuario.email,
            'nome': fisio.funcionario.usuario.first_name,
            'sobrenome': fisio.funcionario.usuario.last_name,
            'cpf': fisio.funcionario.cpf,
            'nascimento': fisio.funcionario.nascimento,
            'contratacao': fisio.funcionario.contratacao,
            'telefone1': fisio.funcionario.telefone1,
            'telefone2': fisio.funcionario.telefone2,
            'endereco': fisio.funcionario.endereco,
            'complemento': fisio.funcionario.complemento,
            'numero': fisio.funcionario.numero,
            'bairro': fisio.funcionario.bairro,
            'cidade': fisio.funcionario.cidade,
            'uf': fisio.funcionario.uf,
            'estado_civil': fisio.funcionario.estado_civil,
            'genero': fisio.funcionario.genero,
            'crefito': fisio.crefito,
            'especializacao': fisio.especializacao,
            'cursos': fisio.cursos,
        }
        context = {
            'object': fisio,
            'form': FisioterapeutaUpdateForm(initial=dados)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """POST"""
        fisio = Fisioterapeuta.objects.get(id=kwargs['pk'])
        form = FisioterapeutaUpdateForm(request.POST or None)
        if form.is_valid():

            clean = form.cleaned_data

            fisio.funcionario.usuario.username = clean['nome_usuario']
            fisio.funcionario.usuario.first_name = clean['nome']
            fisio.funcionario.usuario.last_name = clean['sobrenome']
            fisio.funcionario.usuario.email = clean['email']

            fisio.funcionario.usuario.save(update_fields=[
                'username', 'first_name', 'last_name', 'email',
            ])

            fisio.funcionario.cpf = clean['cpf']
            fisio.funcionario.nascimento = clean['nascimento']
            fisio.funcionario.contratacao = clean['contratacao']
            fisio.funcionario.telefone1 = clean['telefone1']
            fisio.funcionario.telefone2 = clean['telefone2']
            fisio.funcionario.endereco = clean['endereco']
            fisio.funcionario.complemento = clean['complemento']
            fisio.funcionario.numero = clean['numero']
            fisio.funcionario.bairro = clean['bairro']
            fisio.funcionario.cidade = clean['cidade']
            fisio.funcionario.uf = clean['uf']
            fisio.funcionario.estado_civil = clean['estado_civil']
            fisio.funcionario.genero = clean['genero']

            fisio.funcionario.save(update_fields=[
                'cpf', 'nascimento', 'contratacao', 'telefone1', 'telefone2',
                'endereco', 'complemento', 'numero', 'bairro', 'cidade',
                'uf', 'estado_civil', 'genero',
            ])

            fisio.crefito = clean['crefito']
            fisio.especializacao = clean['especializacao']
            fisio.cursos = clean['cursos']

            fisio.save(update_fields={
                'crefito', 'especializacao', 'cursos'
            })

            messages.success(request, 'Dados alterados com sucesso!')

            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})

class EsteticistaCreateView(LoginRequiredMixin, PermissionRequiredMixin, View): # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Funcionarios Esteticistas"""
    template_name = 'funcionarios/esteticista_form.html'
    success_message = "Esteticista adicionado!"
    success_url = reverse_lazy('funcionarios:funcionario_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = {'funcionarios.add_funcionario',
                           'funcionarios.add_esteticista'}

    def get(self, request, *args, **kwargs):
        """GET"""
        return render(request, self.template_name, {'form': EsteticistaCreateForm})

    def post(self, request, *args, **kwargs):
        """POST"""
        form = EsteticistaCreateForm(request.POST, request.FILES or None)
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

            esteticista = Esteticista(
                funcionario=funcionario,
                cursos=clean['cursos']
                )
            esteticista.save()

            messages.success(request,
                             'Esteticista %s adicionado com sucesso!' \
                             % esteticista.funcionario.nome_completo)

            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})

class EsteticistaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View): # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Funcionarios Esteticistas"""
    template_name = 'funcionarios/esteticista_form.html'
    success_message = "Esteticista adicionado!"
    success_url = reverse_lazy('funcionarios:funcionario_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = {'funcionarios.change_funcionario',
                           'funcionarios.change_esteticista'}

    def get(self, request, *args, **kwargs):
        """GET"""
        esteticista = Esteticista.objects.get(id=kwargs['pk'])
        dados = {
            'nome_usuario': esteticista.funcionario.usuario.username,
            'email': esteticista.funcionario.usuario.email,
            'nome': esteticista.funcionario.usuario.first_name,
            'sobrenome': esteticista.funcionario.usuario.last_name,
            'cpf': esteticista.funcionario.cpf,
            'nascimento': esteticista.funcionario.nascimento,
            'contratacao': esteticista.funcionario.contratacao,
            'telefone1': esteticista.funcionario.telefone1,
            'telefone2': esteticista.funcionario.telefone2,
            'endereco': esteticista.funcionario.endereco,
            'complemento': esteticista.funcionario.complemento,
            'numero': esteticista.funcionario.numero,
            'bairro': esteticista.funcionario.bairro,
            'cidade': esteticista.funcionario.cidade,
            'uf': esteticista.funcionario.uf,
            'estado_civil': esteticista.funcionario.estado_civil,
            'genero': esteticista.funcionario.genero,
            'cursos': esteticista.cursos,
        }
        context = {
            'object': esteticista,
            'form': EsteticistaUpdateForm(initial=dados)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """POST"""
        esteticista = Esteticista.objects.get(id=kwargs['pk'])
        form = EsteticistaUpdateForm(request.POST or None)
        if form.is_valid():

            clean = form.cleaned_data

            esteticista.funcionario.usuario.username = clean['nome_usuario']
            esteticista.funcionario.usuario.first_name = clean['nome']
            esteticista.funcionario.usuario.last_name = clean['sobrenome']
            esteticista.funcionario.usuario.email = clean['email']

            esteticista.funcionario.usuario.save(update_fields=[
                'username', 'first_name', 'last_name', 'email',
            ])

            esteticista.funcionario.cpf = clean['cpf']
            esteticista.funcionario.nascimento = clean['nascimento']
            esteticista.funcionario.contratacao = clean['contratacao']
            esteticista.funcionario.telefone1 = clean['telefone1']
            esteticista.funcionario.telefone2 = clean['telefone2']
            esteticista.funcionario.endereco = clean['endereco']
            esteticista.funcionario.complemento = clean['complemento']
            esteticista.funcionario.numero = clean['numero']
            esteticista.funcionario.bairro = clean['bairro']
            esteticista.funcionario.cidade = clean['cidade']
            esteticista.funcionario.uf = clean['uf']
            esteticista.funcionario.estado_civil = clean['estado_civil']
            esteticista.funcionario.genero = clean['genero']

            esteticista.funcionario.save(update_fields=[
                'cpf', 'nascimento', 'contratacao', 'telefone1', 'telefone2',
                'endereco', 'complemento', 'numero', 'bairro', 'cidade',
                'uf', 'estado_civil', 'genero',
            ])

            esteticista.cursos = clean['cursos']

            esteticista.save(update_fields={'cursos'})

            messages.success(request, 'Dados alterados com sucesso!')

            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})
