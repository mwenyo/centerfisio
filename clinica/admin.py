from django.contrib import admin

from .models import TipoTratamento, Procedimento, Pacote, PacoteProcedimento

admin.site.register(TipoTratamento)
admin.site.register(Procedimento)
admin.site.register(Pacote)
admin.site.register(PacoteProcedimento)
