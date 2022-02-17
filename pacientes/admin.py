from django.contrib import admin
from .models import Paciente


# Register your models here.

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    """
        Admin View for Paciente
    """
    list_display = ('nome',
                    'data_nascimento',
                    'cidade',
                    'profissao',
                    'telefone',)
    list_filter = ('nome',)
    search_fields = ('nome',)
