"""Registro Admin Pacientes"""
from django.contrib import admin

from .models import Paciente, Contato

admin.site.register(Paciente)
admin.site.register(Contato)
