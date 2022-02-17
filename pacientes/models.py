from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField("Nascimento", null=True, blank=True)
    cpf = models.CharField("CPF", max_length=14, null=True, blank=True)
    rg = models.CharField("RG", max_length=50, null=True, blank=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(
        "Endereço", max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(
        max_length=200, default="PI", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    profissao = models.CharField(
        "Profissão", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome
