"""Registro Admin Pacientes"""
from django.contrib import admin

from .models import Paciente, Contato

class ContatoInline(admin.TabularInline):
    '''Tabular Inline View for Contato'''

    model = Contato

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    '''Admin View for Paciente'''

    inlines = [
        ContatoInline,
    ]
