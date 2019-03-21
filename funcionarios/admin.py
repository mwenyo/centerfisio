"""Registro dos Models na Administração do Django"""
from django.contrib import admin
from .models import Funcionario, Fisioterapeuta

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Fisioterapeuta)
