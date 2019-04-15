"""Views Clínica"""
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import PacoteForm
from .models import Convenio, Procedimento, Pacote

class ConvenioView(LoginRequiredMixin, PermissionRequiredMixin, ListView): # pylint: disable=too-many-ancestors
    """Lista de Convenios"""
    model = Convenio
    template_name = "clinica/convenio/list.html"
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.view_convenio'

class ConvenioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView): # pylint: disable=too-many-ancestors,line-too-long
    """Editar Convenios"""
    model = Convenio
    fields = ['nome', 'status']
    template_name = "clinica/convenio/form.html"
    success_message = "Alteração realizada com sucesso!"
    success_url = reverse_lazy('clinica:convenio_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.change_convenio'

class ConvenioCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView): # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Convenios"""
    model = Convenio
    fields = ['nome', 'status']
    template_name = "clinica/convenio/form.html"
    success_message = "Convênio adicionado!"
    success_url = reverse_lazy('clinica:convenio_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.add_convenio'

class ConvenioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView): # pylint: disable=too-many-ancestors,line-too-long
    """Excluir Convenios"""
    model = Convenio
    template_name = "clinica/convenio/delete.html"
    success_message = "Convênio excluído!"
    success_url = reverse_lazy('clinica:convenio_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.delete_convenio'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ConvenioDeleteView, self).delete(request, *args, **kwargs)

class ProcedimentoView(LoginRequiredMixin, PermissionRequiredMixin, ListView): # pylint: disable=too-many-ancestors
    """Lista de Procedimentos"""
    model = Procedimento
    template_name = "clinica/procedimento/list.html"
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.view_procedimento'

class ProcedimentoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView): # pylint: disable=too-many-ancestors,line-too-long
    """Editar Procedimentos"""
    model = Procedimento
    fields = ['tipo', 'nome', 'descricao', 'valor_unitario', 'status']
    template_name = "clinica/procedimento/form.html"
    success_message = "Alteração realizada com sucesso!"
    success_url = reverse_lazy('clinica:procedimento_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.change_procedimento'

class ProcedimentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView): # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Procedimentos"""
    model = Procedimento
    fields = ['tipo', 'nome', 'descricao', 'valor_unitario', 'status']
    template_name = "clinica/procedimento/form.html"
    success_message = "Procedimento adicionado!"
    success_url = reverse_lazy('clinica:procedimento_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.add_procedimento'

class ProcedimentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView): # pylint: disable=too-many-ancestors,line-too-long
    """Excluir Procedimentos"""
    model = Procedimento
    template_name = "clinica/procedimento/delete.html"
    success_message = "Procedimento excluído!"
    success_url = reverse_lazy('clinica:procedimento_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.delete_procedimento'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProcedimentoDeleteView, self).delete(request, *args, **kwargs)


class PacoteView(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    """Lista de Pacotes"""
    model = Pacote
    template_name = "clinica/pacote/list.html"
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.view_pacote'


class PacoteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):  # pylint: disable=too-many-ancestors,line-too-long
    """Editar Pacotes"""
    model = Pacote
    form_class = PacoteForm
    #fields = ['nome', 'descricao', 'valor', 'promocao', 'inicio', 'termino', 'status', ]
    template_name = "clinica/pacote/form.html"
    success_message = "Alteração realizada com sucesso!"
    success_url = reverse_lazy('clinica:pacote_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.change_pacote'


class PacoteCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):  # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Pacotes"""
    model = Pacote
    form_class = PacoteForm
    #fields = ['nome', 'descricao', 'valor', 'promocao', 'inicio', 'termino', 'status', ]
    template_name = "clinica/pacote/form.html"
    success_message = "Pacote adicionado!"
    success_url = reverse_lazy('clinica:pacote_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.add_pacote'


class PacoteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):  # pylint: disable=too-many-ancestors,line-too-long
    """Excluir Pacotes"""
    model = Pacote
    template_name = "clinica/pacote/delete.html"
    success_message = "Pacote excluído!"
    success_url = reverse_lazy('clinica:pacote_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.delete_pacote'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PacoteDeleteView, self).delete(request, *args, **kwargs)


class PacoteDetailView(DetailView):
    model = Pacote
    template_name = "clinica/pacote/detail.html"
