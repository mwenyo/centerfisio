from django.contrib import admin

from .models import Tipo, Procedimento, Pacote, PacoteProcedimento

admin.site.register(Tipo)
admin.site.register(Procedimento)
admin.site.register(Pacote)
admin.site.register(PacoteProcedimento)
