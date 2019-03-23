"""View Funcionários"""

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Funcionario, Fisioterapeuta

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    """View da HomePage"""
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        """Coleta de dados do BD"""

        context = super(HomeView, self).get_context_data(**kwargs)
        funcionario = get_object_or_404(Funcionario, id=self.request.user.id)
        fisioterapeuta = Fisioterapeuta.objects.filter(funcionario__id=funcionario.id).first()

        if fisioterapeuta:
            context['fisioterapeuta'] = fisioterapeuta
            return context

        context['funcionario'] = funcionario
        return context
