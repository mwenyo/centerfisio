from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from pacientes.models import Paciente
from pacientes.forms import PacienteForm


class PacienteListView(\
    LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    """Lista de Pacientes"""
    model = Paciente
    template_name = 'pacientes/list.html'
    permission_required = "pacientes.view_paciente"
    login_url = reverse_lazy('admin:login')


class PacienteCreateView(\
    LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Paciente
    template_name = "pacientes/form.html"
    form_class = PacienteForm
    success_url = reverse_lazy('pacientes:paciente_list')
    permission_required = "pacientes.add_paciente"
    login_url = reverse_lazy('admin:login')


class PacienteUpdateView(\
    LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Paciente
    template_name = "pacientes/form.html"
    form_class = PacienteForm
    success_url = reverse_lazy('pacientes:paciente_list')
    permission_required = "pacientes.change_paciente"
    login_url = reverse_lazy('admin:login')


class PacienteDeleteView(\
    LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy('pacientes:paciente_list')
    permission_required = "pacientes.delete_paciente"
    login_url = reverse_lazy('admin:login')



class PacienteDetailView(\
    LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Paciente
    template_name = "pacientes/detail.html"
    permission_required = "pacientes.view_paciente"
    login_url = reverse_lazy('admin:login')


class PacienteListAjaxView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = "pacientes.view_paciente"
    login_url = reverse_lazy('admin:login')

    def get(self, request):
        pacientes = serializers.serialize('json',
                                          Paciente.objects.all()
                                          .order_by('nome'),
                                          fields=('id', 'nome', 'telefone',))
        return HttpResponse(pacientes, content_type="application/json")


class PacienteCreateAjaxView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "pacientes.add_paciente"
    login_url = reverse_lazy('admin:login')

    def post(self, request):
        nome = request.POST.get('nome', '')
        telefone = request.POST.get('telefone', '')
        paciente = Paciente(nome=nome, telefone=telefone)
        paciente.save()
        return JsonResponse(model_to_dict(paciente), status=200)
