"""Models de Estética"""
from django.db import models

class Procedimento(models.Model):
    """Model definition for Procedimento."""

    nome = models.CharField(max_length=200)
    descricao = models.TextField("Descrição")
    valor_unitario = models.FloatField("Valor Unitário", default=0.0)

    def __str__(self):
        """Unicode representation of Procedimento."""
        return self.nome

class Pacote(models.Model):
    """Model definition for Pacote."""

    nome = models.CharField(max_length=200)
    descricao = models.TextField("Descrição")
    valor = models.FloatField(default=0)

    def __str__(self):
        """Unicode representation of Pacote."""
        return self.nome

class PacoteProcedimento(models.Model):
    """Model definition for PacoteProcedimento."""

    pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for PacoteProcedimento."""

        verbose_name = 'Pacote de Procedimentos'
        verbose_name_plural = 'Pacotes de Procedimentos'

    def __str__(self):
        """Unicode representation of PacoteProcedimento."""
        return self.pacote + ' - ' + self.procedimento
