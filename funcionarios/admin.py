"""Registro dos Models na Administração do Django"""
from django.contrib import admin
from .models import Funcionario, Fisioterapeuta, Esteticista, Instrutor, Administrador

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Fisioterapeuta)
admin.site.register(Esteticista)
admin.site.register(Instrutor)
admin.site.register(Administrador)
