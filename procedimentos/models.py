""" MODELS DO APP PROCEDIMENTOS """
from django.db import models


# Create your models here.

class Procedimento(models.Model):
    """ MODEL PROCEDIMENTOS """
    class TipoAtendimentoChoices(models.IntegerChoices):
        ESTETICA = 0, 'ESTÉTICA'
        FISIOTERAPIA = 1, 'FISIOTERAPIA'

    nome = models.CharField(max_length=200)
    descricao = models.TextField("Descrição", null=True, blank=True)
    duracao = models.TimeField("Duração", null=True, blank=True)
    valor = models.DecimalField(
        "Valor", max_digits=5, decimal_places=2, default=0.0)
    tipo_atendimento = models.SmallIntegerField(
        "Tipo de Atendimento", choices=TipoAtendimentoChoices.choices,
        default=TipoAtendimentoChoices.ESTETICA)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Promocao(models.Model):
    """ MODEL PROMOCAO """
    descricao = models.CharField(max_length=200)
    inicio = models.DateField("Início", null=True, blank=True)
    termino = models.DateField("Término", null=True, blank=True)
    procedimentos = models.ManyToManyField(
        Procedimento, through="ProcedimentoPromocao", blank=True)

    class Meta:
        verbose_name = "Promoção"
        verbose_name_plural = "Promoções"
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


class ProcedimentoPromocao(models.Model):
    """
        MODEL INTERMEDIÁRIO ENTRE PROMOÇÃO E PROCEDIMENTO
    """
    promocao = models.ForeignKey(Promocao, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    valor_promocional = models.DecimalField("Valor Promocional",
                                            max_digits=5,
                                            decimal_places=2,
                                            default=0.0)

    class Meta:
        verbose_name = "Procedimento em Promoção"
        verbose_name_plural = "Procedimentos em Promoções"
        unique_together = ['promocao', 'procedimento']
        order_with_respect_to = 'procedimento'

    def __str__(self):
        return self.promocao.descricao + " - " + self.procedimento.nome
