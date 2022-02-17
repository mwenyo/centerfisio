from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.urls import reverse_lazy

from pacientes.models import Paciente


class Index(\
    LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'base.html'
    permission_required = "movimentacoes.view_usuario"
    login_url = reverse_lazy('admin:login')

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        # here's the difference:
        context['pacientes_cadastrados'] = Paciente.objects.count()
        return context
