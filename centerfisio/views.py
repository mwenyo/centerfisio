"""Views do Funcionário"""
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from funcionarios.models import Funcionario

def home(request):
    """Exibir página inicial do sistema"""
    funcionario = get_object_or_404(Funcionario, id=request.user.id)
    return render_to_response('html/base.html', {'user': funcionario})
