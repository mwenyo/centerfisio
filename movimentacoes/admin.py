from django.contrib import admin

from .models import Usuario
from .models import Agendamento
from .models import Caixa
from .models import FormaDePagamento
from .models import AgendamentoPagamento
from .models import Movimentacao

# from .models import Atendimento

# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'funcao')


@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    list_display = ('data', 'abertura', 'fechamento', 'status')
    list_filter = ('data',)
    search_fields = ('data',)


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    """
        Admin View for Agendamento
    """
    list_display = ('paciente',
                    'usuario',
                    'data',
                    'horario', 'status')
    list_filter = ('data',)
    search_fields = ('paciente__nome',)


@admin.register(FormaDePagamento)
class FormaDePagamentoAdmin(admin.ModelAdmin):
    """
        Admin View for FormaDePagamento
    """
    list_display = ('nome',
                    'acrescimo',
                    'desconto')


@admin.register(AgendamentoPagamento)
class AgendamentoPagamentoAdmin(admin.ModelAdmin):
    """
        Admin View for AgendamentoPagamento
    """
    list_display = ('agendamento',
                    'caixa',
                    'forma_pagamento',
                    'valor_pago')


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    """
        Admin View for Movimentacao
    """
    list_display = ('usuario',
                    'caixa',
                    'forma_pagamento',
                    'descricao', 'natureza', 'tipo', 'horario', 'valor')
