from django.db import models
from django.contrib.auth.models import User

from pacientes.models import Paciente
from procedimentos.models import Procedimento, ProcedimentoPromocao


class Usuario(models.Model):
    class FuncaoDoUsuario(models.IntegerChoices):
        ADMINISTRADOR = 1, 'ADMINISTRADOR'
        ESTETICISTA = 2, 'ESTETICISTA'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    funcao = models.SmallIntegerField("Função",
                                      choices=FuncaoDoUsuario.choices,
                                      default=FuncaoDoUsuario.ESTETICISTA
                                      )

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.user.first_name


class Caixa(models.Model):
    operador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField()
    abertura = models.TimeField()
    fechamento = models.TimeField(null=True, blank=True)
    saldo_inicial = models.DecimalField(
        "Saldo Inicial", max_digits=7, decimal_places=2, null=True, blank=True)
    saldo = models.DecimalField(
        "Saldo", max_digits=7, decimal_places=2, null=True, blank=True)
    status = models.BooleanField("Aberto", default=1)

    class Meta:
        verbose_name = "Caixa"
        verbose_name_plural = "Caixas"

    def __str__(self):
        return str(self.data)


class Agendamento(models.Model):
    class SituacaoDoAgendamento(models.IntegerChoices):
        ACONFIRMAR = 0, 'A CONFIRMAR'
        CONFIRMADO = 1, 'CONFIRMADO'
        EMESPERA = 2, 'EM ESPERA'
        EMATENDIMENTO = 3, 'EM ATENDIMENTO'
        ENCERRADO = 4, 'ENCERRADO'

    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,
                                on_delete=models.CASCADE)
    profissional = models.ForeignKey(Usuario, related_name="profissional",
                                     on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField("Horário")
    observacoes = models.TextField("Observações",
                                   null=True,
                                   blank=True)
    status = models.SmallIntegerField(
        "Situação",
        choices=SituacaoDoAgendamento.choices,
        default=SituacaoDoAgendamento.ACONFIRMAR
    )
    procedimentos = models.ManyToManyField(Procedimento,
                                           blank=True)
    procedimentos_promo = models.ManyToManyField(
        ProcedimentoPromocao,
        verbose_name="Procedimentos em Promoção",
        blank=True
    )
    valor = models.DecimalField(
        "Valor", max_digits=7, decimal_places=2, default=0)

    valor_diferenciado = models.BooleanField(
        "Valor Diferenciado", default=False)

    desconto = models.DecimalField(
        "Desconto", max_digits=7, decimal_places=2, default=0,
        null=True, blank=True)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        unique_together = ['profissional', 'horario', 'data']

    def __str__(self):
        return self.paciente.nome + " - " + \
            self.usuario.user.first_name + " - " + \
            str(self.data) + " " + str(self.horario)


class FormaDePagamento(models.Model):
    nome = models.CharField("Descrição", max_length=50)
    acrescimo = models.DecimalField("Acréscimo",
                                    max_digits=6,
                                    decimal_places=4,
                                    default=0,
                                    null=True,
                                    blank=True)
    desconto = models.DecimalField("Desconto",
                                   max_digits=6,
                                   decimal_places=4,
                                   default=0,
                                   null=True,
                                   blank=True)

    class Meta:
        verbose_name = "Forma de Pagamento"
        verbose_name_plural = "Formas de Pagamentos"

    def __str__(self):
        return self.nome


class AgendamentoPagamento(models.Model):
    agendamento = models.ForeignKey(
        Agendamento, on_delete=models.CASCADE)
    caixa = models.ForeignKey(
        Caixa, on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey(
        FormaDePagamento, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(
        "Valor Pago", max_digits=5, decimal_places=2)
    horario = models.DateTimeField("Horário", null=True, blank=True)

    class Meta:
        verbose_name = "Registro de Pagamento do Agendamento"
        verbose_name_plural = "Registros de Pagamentos dos Agendamentos"


class Movimentacao(models.Model):
    class TipoMovimentacao(models.IntegerChoices):
        ENTRADA = 0, 'ENTRADA'
        SAIDA = 1, 'SAÍDA'

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey(
        FormaDePagamento, on_delete=models.CASCADE)
    descricao = models.TextField("Descrição")
    natureza = models.CharField(max_length=200)
    tipo = models.SmallIntegerField(
        choices=TipoMovimentacao.choices,
        default=TipoMovimentacao.ENTRADA)
    horario = models.DateTimeField("Horário")
    valor = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = "Registro de Movimentação"
        verbose_name_plural = "Registros de Movimentações"
