"""View Funcionários"""

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Funcionario

@login_required(login_url="/admin/login")
def home(request):
    """Exibir página inicial do sistema"""
    funcionario = get_object_or_404(Funcionario, id=request.user.id)
    return render_to_response('html/base.html', {'user': funcionario})
