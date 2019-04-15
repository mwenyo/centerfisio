"""Models de Clínica"""
from django.db import models

from funcionarios.models import Administrador, Fisioterapeuta, Esteticista
from pacientes.models import Paciente

class Tipo(models.Model):
    """Model definition for Tipo."""

    nome = models.CharField("Tipo de tratamento", max_length=200)

    class Meta:
        """Meta definition for Tipo."""

        verbose_name = 'Tipo de Tratamento'
        verbose_name_plural = 'Tipos de Tratamentos'

    def __str__(self):
        """Unicode representation of Tipo."""
        return self.nome

class Procedimento(models.Model):
    """Model definition for Procedimento."""

    ATIVO = 1
    INATIVO = 0

    STATUS_CHOICES = (
        (1, "ATIVO"),
        (0, "INATIVO"),
    )

    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField("Descrição")
    valor_unitario = models.FloatField("Valor Unitário", default=0.0)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=ATIVO)


    def __str__(self):
        """Unicode representation of Procedimento."""
        return self.nome

class Pacote(models.Model):
    """Model definition for Pacote."""

    STATUS_CHOICES = (
        (1, "ATIVO"),
        (0, "INATIVO"),
    )

    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField("Descrição")
    valor = models.FloatField(default=0)
    promocao = models.BooleanField("Promoção", default=False)
    inicio = models.DateField("Data Inicial", \
        auto_now=False, auto_now_add=False, null=True, blank=True)
    termino = models.DateField("Data Final", \
        auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)
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

class Convenio(models.Model):
    """Model definition for Convenio."""
    ATIVO = 1
    INATIVO = 0

    STATUS_CHOICES = (
        (ATIVO, "ATIVO"),
        (INATIVO, "INATIVO"),

    )

    nome = models.CharField(max_length=200)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=ATIVO)


    class Meta:
        """Meta definition for Convenio."""

        verbose_name = 'Convênio'
        verbose_name_plural = 'Convênios'

    def __str__(self):
        """Unicode representation of Convenio."""
        return self.nome

class Prontuario(models.Model):
    """Model definition for Prontuario."""

    ATIVO = 1
    INATIVO = 0

    STATUS_CHOICES = (
        (ATIVO, "ATIVO"),
        (INATIVO, "INATIVO"),

    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    data_cadastro = models.DateField("Data Cadastro", auto_now=False, auto_now_add=True)
    queixa = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=ATIVO)

    class Meta:
        """Meta definition for Prontuario."""

        verbose_name = 'Prontuário'
        verbose_name_plural = 'Prontuários'

    def __str__(self):
        """Unicode representation of Prontuario."""
        return self.paciente.nome + " - " + self.tipo.nome + ' - ' + self.queixa

class ProcedimentoProntuario(models.Model):
    """Model definition for ProcedimentoProntuario."""

    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for ProcedimentoProntuario."""

        verbose_name = 'Procedimento de Prontuario'
        verbose_name_plural = 'Procedimentos de Prontuarios'

    def __str__(self):
        """Unicode representation of ProcedimentoProntuario."""
        return str(self.prontuario) + " - " + str(self.procedimento)

class Sessao(models.Model):
    """Model definition for Sessao."""

    REALIZADA = 1
    CANCELADA = 0
    CONFIRMADA = 2
    ACONFIRMAR = 3

    STATUS_CHOICES = (
        (REALIZADA, "REALIZADA"),
        (CANCELADA, "CANCELADA"),
        (CONFIRMADA, "CONFIRMADA"),
        (ACONFIRMAR, "À CONFIRMAR"),
    )

    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    procedimento_prontuario = models.ForeignKey(ProcedimentoProntuario, on_delete=models.CASCADE)
    data_agendamento = models.DateField("Data de Agendamento", auto_now=False, auto_now_add=False)
    horario_agendamento = models.TimeField("Horário de Agendamento", \
        auto_now=False, auto_now_add=False)
    conduta = models.TextField(null=True, blank=True)
    status = models.PositiveSmallIntegerField("Situação", choices=STATUS_CHOICES)

    class Meta:
        """Meta definition for Sessao."""

        verbose_name = 'Sessão'
        verbose_name_plural = 'Sessões'

    def __str__(self):
        """Unicode representation of Sessao."""
        return str(self.procedimento_prontuario) + ' - ' + str(self.data_agendamento) + " " + \
            str(self.horario_agendamento)

class SessaoFisioterapia(models.Model):
    """Model definition for SessaoFisioterapia."""

    fisioterapeuta = models.ForeignKey(Fisioterapeuta, on_delete=models.CASCADE)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for SessaoFisioterapia."""

        verbose_name = 'Sessão de Fisioterapia'
        verbose_name_plural = 'Sessões de Fisioterapia'

    def __str__(self):
        """Unicode representation of Sessao."""
        return str(self.fisioterapeuta) + " - " + str(self.sessao)

class SessaoEstetica(models.Model):
    """Model definition for SessaoEstetica."""

    esteticista = models.ForeignKey(Esteticista, on_delete=models.CASCADE)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for SessaoEstetica."""

        verbose_name = 'Sessão de Estetica'
        verbose_name_plural = 'Sessões de Estetica'

    def __str__(self):
        """Unicode representation of Sessao."""
        return str(self.esteticista) + " - " + str(self.sessao)
