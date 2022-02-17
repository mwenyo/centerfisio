from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.db.models import Q, Subquery
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import formats
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView

from .models import Procedimento
from .models import Promocao
from .models import ProcedimentoPromocao

from .forms import ProcedimentoForm
from .forms import PromocaoForm

# PROCEDIMENTOS #


class ProcedimentoListView(\
    LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Procedimento
    template_name = "procedimento/list.html"
    permission_required = "procedimentos.view_procedimento"
    login_url = reverse_lazy('admin:login')


class ProcedimentoAjaxListView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "procedimentos.view_procedimento"
    login_url = reverse_lazy('admin:login')

    def post(self, request, id):
        pd = Procedimento.objects.all().exclude(
            procedimentopromocao__promocao__id=id)
        return render(request, "procedimento/list_ajax.html",
                      context={'context': pd})


class ProcedimentoCreateView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    """ Lista de Formas de Pagamento """

    permission_required = "procedimentos.add_procedimento"
    login_url = reverse_lazy('admin:login')

    def post(self, request):
        form = ProcedimentoForm(request.POST)
        if form.is_valid and request.is_ajax():
            form.save()
            procedimento = form.instance
            return JsonResponse(model_to_dict(procedimento), status=200)
        else:
            return JsonResponse(
                {'result': 'formulario invalido'},
                status=200)


class ProcedimentoUpdateView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    """ Lista de Formas de Pagamento """

    permission_required = "procedimentos.change_procedimento"
    login_url = reverse_lazy('admin:login')

    def post(self, request, id):
        procedimento = get_object_or_404(Procedimento, pk=id)
        form = ProcedimentoForm(request.POST, instance=procedimento)
        if form.is_valid and request.is_ajax():
            form.save()
            procedimento = get_object_or_404(Procedimento, pk=id)
            return JsonResponse(model_to_dict(procedimento), status=200)
        else:
            return JsonResponse(
                {'result': 'formulario invalido'},
                status=200)


class ProcedimentoDeleteView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    """ Lista de Formas de Pagamento """

    permission_required = "procedimentos.delete_procedimento"
    login_url = reverse_lazy('admin:login')

    def post(self, request, id):
        procedimento = get_object_or_404(Procedimento, pk=id)
        procedimento.delete()
        return JsonResponse({'result': 'ok'}, status=200)


# PROMOÇÕES #


class PromocaoListView(\
    LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Promocao
    template_name = "promocao/list.html"
    permission_required = "procedimentos.view_promocao"
    login_url = reverse_lazy('admin:login')


class PromocaoDetailView(\
    LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Promocao
    template_name = "promocao/detail.html"
    permission_required = "procedimentos.view_promocao"
    login_url = reverse_lazy('admin:login')


class PromocaoCreateView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    """ Lista de Formas de Pagamento """
    permission_required = "procedimentos.add_promocao"
    login_url = reverse_lazy('admin:login')

    def post(self, request):
        form = PromocaoForm(request.POST)
        if form.is_valid and request.is_ajax():
            form.save()
            promocao = form.instance
            promocao.inicio = formats.date_format(
                promocao.inicio, r'j \d\e F \d\e Y')
            promocao.termino = formats.date_format(
                promocao.termino, r'j \d\e F \d\e Y')
            return JsonResponse(model_to_dict(promocao), status=200)
        else:
            return JsonResponse(
                {'result': 'formulario invalido'},
                status=200)


class PromocaoUpdateView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    """ Lista de Formas de Pagamento """

    permission_required = "procedimentos.change_promocao"
    login_url = reverse_lazy('admin:login')

    def post(self, request, id):
        promocao = get_object_or_404(Promocao, pk=id)
        form = PromocaoForm(request.POST, instance=promocao)
        if form.is_valid and request.is_ajax():
            form.save()
            promocao = get_object_or_404(Promocao, pk=id)
            promocao.inicio = formats.date_format(
                promocao.inicio, r'j \d\e F \d\e Y')
            promocao.termino = formats.date_format(
                promocao.termino, r'j \d\e F \d\e Y')
            return JsonResponse(
                model_to_dict(
                    promocao, fields=[
                        field.name for field in promocao._meta.fields
                    ]), status=200)
        else:
            return JsonResponse(
                {'result': 'formulario invalido'},
                status=200)


class PromocaoDeleteView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    """ Lista de Formas de Pagamento """

    permission_required = "procedimentos.delete_promocao"
    login_url = reverse_lazy('admin:login')

    def get(self, request, id):
        return JsonResponse({'mensagem': 'veio pelo get'}, status=200)

    def post(self, request, id):
        promocao = get_object_or_404(Promocao, pk=id)
        promocao.delete()
        return JsonResponse({'result': 'ok'}, status=200)


# PROCEDIMENTOS EM PROMOÇÃO #


class ProcedimentoPromocaoCreateView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    """ Lista de Formas de Pagamento """

    permission_required = "procedimentos.add_procedimentopromocao"
    login_url = reverse_lazy('admin:login')

    def post(self, request):
        promocao = request.POST.get('promocao', '')
        procedimento = request.POST.get('procedimento', '')
        valor_promocional = request.POST.get('valor_promocional', '')
        procedimento_promocao = ProcedimentoPromocao(
            None,
            promocao,
            procedimento,
            valor_promocional)
        procedimento_promocao.save()

        procedimento = Procedimento.objects.get(
            id=procedimento_promocao.procedimento.id)

        context = {}
        context['procedimento'] = model_to_dict(procedimento)
        context['procedimento_promocao'] = model_to_dict(procedimento_promocao)

        return JsonResponse(context, status=200)


class ProcedimentoAjaxListView2(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "procedimentos.view_procedimentopromocao"
    login_url = reverse_lazy('admin:login')
    
    def get(self, request):
        procedimentos = serializers.serialize('json',
                                              Procedimento.objects.all(),
                                              fields=('id', 'nome', 'valor',))
        return HttpResponse(procedimentos, content_type="application/json")


class ProcedimentoPromocaoUpdateView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    """ Lista de Formas de Pagamento """
    permission_required = "procedimentos.change_procedimentopromocao"
    login_url = reverse_lazy('admin:login')

    def post(self, request, id):
        procedimento_promocao = get_object_or_404(ProcedimentoPromocao, pk=id)
        procedimento_promocao.valor_promocional = request.POST.get(
            'valor_promocional', '')
        procedimento_promocao.save()
        return JsonResponse(
            {'valor_promocional': procedimento_promocao.valor_promocional},
            status=200)


class ProcedimentoPromocaoDeleteView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    """ Lista de Formas de Pagamento """
    permission_required = "procedimentos.delete_procedimentopromocao"
    login_url = reverse_lazy('admin:login')

    def post(self, request, id):
        procedimento_promocao = get_object_or_404(ProcedimentoPromocao, pk=id)
        procedimento_promocao.delete()
        return JsonResponse({'result': 'ok'}, status=200)


class ProcedimentoPromocaoAjaxListView(\
    LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "procedimentos.view_procedimentopromocao"
    login_url = reverse_lazy('admin:login')

    def get(self, request):
        pp = ProcedimentoPromocao.objects.filter(
            Q(promocao__termino__gte=timezone.now()),
            Q(promocao__inicio__lte=timezone.now())
        ).order_by('promocao__inicio', 'procedimento__nome')

        promocoes = Promocao.objects.filter(
            id__in=Subquery(pp.values('promocao'))
        ).values('id', 'descricao')

        # p = Procedimento.objects.filter(
        #     id__in=Subquery(pp.values('procedimento')))
        # all = [*pp, *p]
        # data = serializers.serialize('json', pp, indent=4)

        return render(request, "procedimentopromocao/list_ajax.html",
                      context={
                          'procedimentos_promocoes': pp,
                          'promocoes': promocoes
                      })
