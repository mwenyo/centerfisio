"""Views Clínica"""
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import PacoteForm
from .models import Convenio, Procedimento, Pacote, PacoteProcedimento, Tipo

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
    template_name = "clinica/pacote/form.html"
    success_message = "Alteração realizada com sucesso!"
    success_url = reverse_lazy('clinica:pacote_lista')
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.change_pacote'


class PacoteCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):  # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Pacotes"""
    model = Pacote
    form_class = PacoteForm
    template_name = "clinica/pacote/form.html"
    success_message = "Pacote adicionado!"
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.add_pacote'

    def get_success_url(self):
        return reverse_lazy('clinica:pacote_detalhes', kwargs={'pk': self.object.id})


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


class PacoteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors,line-too-long
    """Detalhes do Pacote"""
    model = Pacote
    template_name = "clinica/pacote/detail.html"
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.view_pacote'


class PacoteProcedimentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):  # pylint: disable=too-many-ancestors,line-too-long
    """Excluir Pacotes"""
    model = PacoteProcedimento
    success_message = "Ítem removido do Pacote!"
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.delete_pacoteprocedimento'
    parent = None

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        self.parent = self.get_object().pacote.id
        return super(PacoteProcedimentoDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """Redirecionamento"""
        return reverse_lazy('clinica:pacote_detalhes', kwargs={'pk': self.parent})


class PacoteProcedimentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, View):  # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar procedimentos ao Pacote"""
    template_name = "clinica/pacote/pacoteprocedimento_form.html"
    login_url = reverse_lazy('admin:login')
    permission_required = 'clinica.add_pacoteprocedimento'

    def get(self, request, *args, **kwargs):
        """GET"""
        pacote = get_object_or_404(Pacote, pk=kwargs['pk'])
        tipo = get_object_or_404(Tipo, id=pacote.tipo.id)
        procedimentos = Procedimento.objects.filter(tipo=tipo, status=Procedimento.ATIVO)
        context = {
            'object' : pacote,
            'procedimentos' : procedimentos
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """POST"""
        data = request.POST.copy()
        pacote_id, quantidade, procedimento_id = data.get('pacote'), \
            int(data.get('quantidade', '1')), data.get('procedimento')

        pacote = get_object_or_404(Pacote, id=pacote_id)
        procedimento = get_object_or_404(Procedimento, id=procedimento_id)

        for i in range(quantidade): #pylint: disable=unused-variable
            item = PacoteProcedimento(pacote=pacote, procedimento=procedimento)
            item.save()

        if quantidade > 1:
            messages.success(request, 'Procedimentos adicionados ao pacote %s' % (pacote.nome))
        else:
            messages.success(
                request,
                'Procedimento %s adicionado ao pacote %s' % (procedimento.nome, pacote.nome)
                )

        return HttpResponseRedirect(
            reverse_lazy('clinica:pacote_detalhes', kwargs={'pk': pacote.id})
            )
