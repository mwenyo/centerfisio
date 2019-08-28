"""View do App Paciente"""
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Paciente
from .forms import PacienteForm, ContatoFormSet

class PacienteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    """Lista de Pacientes"""
    model = Paciente
    template_name = 'pacientes/list.html'
    login_url = reverse_lazy('admin:login')
    permission_required = 'pacientes.view_paciente'


class PacienteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    """Detallhes do Paciente"""
    model = Paciente
    template_name = "pacientes/detail.html"
    login_url = reverse_lazy('admin:login')
    permission_required = 'pacientes.view_paciente'


class PacienteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):  # pylint: disable=too-many-ancestors,line-too-long
    """Editar Pacientes"""
    model = Paciente
    form_class = PacienteForm
    template_name = "pacientes/form.html"
    success_message = "Alteração realizada com sucesso!"
    success_url = reverse_lazy('pacientes:paciente_list')
    login_url = reverse_lazy('admin:login')
    permission_required = 'paciente.change_paciente'
    object = None

    def get_object(self, queryset=None):
        self.object = super(PacienteUpdateView, self).get_object()
        return self.object

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        contato_formset = ContatoFormSet(
            instance=self.object
            )
        return self.render_to_response(
            self.get_context_data(
                form=PacienteForm(instance=self.object),
                contato_formset=contato_formset,
            )
        )

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = PacienteForm(data=self.request.POST, instance=self.object)
        contato_formset = ContatoFormSet(
            data=self.request.POST,
            instance=self.object
        )
        if form.is_valid() and contato_formset.is_valid():
            return self.form_valid(form, contato_formset)
        return self.form_invalid(form, contato_formset)

    def form_valid(self, form, contato_formset):
        self.object = form.save()
        contatos = contato_formset.save(commit=False)
        for obj in contato_formset.deleted_objects:
            obj.delete()

        for contato in contatos:
            contato.instance = self.object
            contato.save()
        messages.success(self.request, self.success_message)
        if '_continue' in self.request.POST:
            return HttpResponseRedirect(
                reverse_lazy(
                    'pacientes:paciente_editar',
                    kwargs={
                        'pk': self.get_object().pk
                    }
                )
            )
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, contato_formset):  # pylint: disable=arguments-differ
        return self.render_to_response(
            self.get_context_data(
                form=form,
                contato_formset=contato_formset
            )
        )

class PacienteCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):  # pylint: disable=too-many-ancestors,line-too-long
    """Adicionar Pacientes"""
    model = Paciente
    form_class = PacienteForm
    template_name = "pacientes/form.html"
    success_message = "Paciente adicionado!"
    success_url = reverse_lazy('pacientes:paciente_list')
    login_url = reverse_lazy('admin:login')
    permission_required = 'paciente.add_paciente'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        contato_formset = ContatoFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  contato_formset=contato_formset))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        contato_formset = ContatoFormSet(self.request.POST)
        if (form.is_valid() and contato_formset.is_valid()):
            return self.form_valid(form, contato_formset)
        return self.form_invalid(form, contato_formset)

    def form_valid(self, form, formset=None):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        paciente = form.save()
        contatos = formset.save(commit=False)
        for contato in contatos:
            contato.instance = paciente
            contato.save()
        return super().form_valid(form)

    def form_invalid(self, form, contato_formset):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.

        Args:
            form: Assignment Form
            contato_formset: Assignment Question Form
        """
        return self.render_to_response(
            self.get_context_data(
                form=form,
                contato_formset=contato_formset
            )
        )

class PacienteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):  # pylint: disable=too-many-ancestors,line-too-long
    """Excluir Pacientes"""
    model = Paciente
    template_name = "pacientes/delete.html"
    success_message = "Paciente excluído!"
    success_url = reverse_lazy('pacientes:paciente_list')
    login_url = reverse_lazy('admin:login')
    permission_required = 'paciente.delete_paciente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PacienteDeleteView, self).delete(request, *args, **kwargs)
