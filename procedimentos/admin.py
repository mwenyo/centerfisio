from django.contrib import admin
from .models import Procedimento
from .models import ProcedimentoPromocao
from .models import Promocao

# Register your models here.


class PromocaoAdmin(admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('descricao', 'inicio', 'termino')


admin.site.register(Promocao, PromocaoAdmin)


class ProcedimentoPromocaoAdmin(admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('promocao', 'procedimento', 'valor_promocional')


admin.site.register(ProcedimentoPromocao, ProcedimentoPromocaoAdmin)


class ProcedimentoAdmin(admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('nome', 'descricao', 'valor', 'tipo_atendimento')


admin.site.register(Procedimento, ProcedimentoAdmin)
