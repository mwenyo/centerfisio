"""Models de Estética"""
from django.db import models

class TipoTratamento(models.Model):
    """Model definition for TipoTratamento."""

    nome = models.CharField("Nome do tratamento", max_length=200)

    class Meta:
        """Meta definition for TipoTratamento."""

        verbose_name = 'Tipo de Tratamento'
        verbose_name_plural = 'Tipos de Tratamentos'

    def __str__(self):
        """Unicode representation of TipoTratamento."""
        return self.nome


class Procedimento(models.Model):
    """Model definition for Procedimento."""

    STATUS_CHOICES = (
        (1, "ATIVO"),
        (0, "INATIVO"),
    )

    tipo = models.ForeignKey(TipoTratamento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField("Descrição")
    valor_unitario = models.FloatField("Valor Unitário", default=0.0)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)


    def __str__(self):
        """Unicode representation of Procedimento."""
        return self.nome

class Pacote(models.Model):
    """Model definition for Pacote."""

    STATUS_CHOICES = (
        (1, "ATIVO"),
        (0, "INATIVO"),
    )

    tipo = models.ForeignKey(TipoTratamento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField("Descrição")
    valor = models.FloatField(default=0)
    promocao = models.BooleanField("Promoção", default=False)
    inicio = models.DateField("Data Inicial", \
        auto_now=False, auto_now_add=False, null=True, blank=True)
    termino = models.DateField("Data Final", \
        auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    procedimentos = models.ManyToManyField(Procedimento, through='PacoteProcedimento')

    def __str__(self):
        """Unicode representation of Pacote."""
        return self.nome

class PacoteProcedimento(models.Model):
    """Model definition for PacoteProcedimento."""

    pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for PacoteProcedimento."""

        verbose_name = 'Pacote de procedimentos'
        verbose_name_plural = 'Pacotes de Procedimentos'

    def __str__(self):
        """Unicode representation of PacoteProcedimento."""
        return self.pacote.nome + ' - ' + self.procedimento.nome
