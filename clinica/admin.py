from django.contrib import admin

from .models import Tipo, Procedimento, Pacote, \
    PacoteProcedimento, ProcedimentoProntuario, Prontuario, Convenio

admin.site.register(Tipo)
admin.site.register(Procedimento)
admin.site.register(Pacote)
admin.site.register(PacoteProcedimento)
admin.site.register(Convenio)
admin.site.register(Prontuario)
admin.site.register(ProcedimentoProntuario)
