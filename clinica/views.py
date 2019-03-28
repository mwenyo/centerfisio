"""Views Clínica"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Convenio

@method_decorator(login_required, name='dispatch')
class ConvenioView(ListView):
    """Lista de Convenios"""
    model = Convenio
    template_name = "clinica/convenio/list.html"

@method_decorator(login_required, name='dispatch')
class ConvenioUpdateView(SuccessMessageMixin, UpdateView): # pylint: disable=too-many-ancestors
    """Editar Convenios"""
    model = Convenio
    fields = ['nome', 'status']
    template_name = "clinica/convenio/form.html"
    success_message = "Alteração realizada com sucesso!"
    success_url = reverse_lazy('clinica:convenio_lista')

@method_decorator(login_required, name='dispatch')
class ConvenioCreateView(SuccessMessageMixin, CreateView):
    """Adicionar Convenios"""
    model = Convenio
    fields = ['nome', 'status']
    template_name = "clinica/convenio/form.html"
    success_message = "Convênio adicionado!"
    success_url = reverse_lazy('clinica:convenio_lista')

@method_decorator(login_required, name='dispatch')
class ConvenioDeleteView(SuccessMessageMixin, DeleteView):
    """Excluir Convenios"""
    model = Convenio
    template_name = "clinica/convenio/delete.html"
    success_message = "Convênio excluído!"
    success_url = reverse_lazy('clinica:convenio_lista')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ConvenioDeleteView, self).delete(request, *args, **kwargs)
