"""Aplicativo Pascientes"""
from django.db import models

# Create your models here.

class Paciente(models.Model):
    """Model definition for Paciente."""

    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AM', 'Amazonas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins'),
    )

    ESTADO_CIVIL_CHOICES = (
        ('Solteiro(a)', 'Solteiro(a)'),
        ('Casado(a)', 'Casado(a)'),
        ('Divorciado(a)', 'Divorciado(a)'),
        ('Viúvo(a)', 'Viúvo(a)'),
        ('União Estável', 'União Estável'),
    )

    GENERO_CHOICE = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
        ('nd', 'Não declarado'),
    )

    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    cpf = models.CharField("CPF", max_length=14, null=False)
    nascimento = models.DateField("Data de nascimento", null=False)
    telefone1 = models.CharField("Telefone", max_length=20)
    telefone2 = models.CharField("Telefone 2", max_length=20, null=True, blank=True)
    genero = models.CharField("Gênero", choices=GENERO_CHOICE, max_length=2,\
        null=True, blank=True)
    estado_civil = models.CharField("Estado civíl", choices=ESTADO_CIVIL_CHOICES, \
        max_length=50, null=True, blank=True)
    profissao = models.CharField("Profissão", max_length=200, default="Desempregado")
    endereco = models.CharField("Endereço", max_length=200, null=True, blank=True)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    numero = models.PositiveSmallIntegerField("Número", null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    uf = models.CharField('Estado', choices=UF_CHOICES, max_length=2,\
        null=True, blank=True)
    diabetes = models.BooleanField(default=False)
    hipertensao = models.BooleanField('Hipertensão', default=False)
    observacoes = models.TextField('Observações', null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    @property
    def nome_completo(self):
        """Retorna o nome completo do paciente"""

        return "%s %s" % (self.nome, self.sobrenome)

    @property
    def imc(self):
        """Retorna o IMC do Paciente"""
        try:
            resultado = self.peso / self.altura ** 2
            return resultado
        except Exception:  # pylint: disable=broad-except
            return "Impossível de calcular"

    @property
    def imc_escala(self):
        """Retorna o IMC do Paciente"""
        try:
            float(self.imc)
            if self.imc >= 40:
                return '<span class="text-danger">Obesidade III</span>'
            elif self.imc >= 35 and self.imc < 40:
                return '<span class = "text-danger"> Obesidade II</span>'
            elif self.imc >= 30 and self.imc < 35:
                return '<span class = "text-danger"> Obesidade I</span>'
            elif self.imc >= 25 and self.imc < 30:
                return '<span class = "text-warning">Sobrepeso</span>'
            elif self.imc >= 18.5 and self.imc < 25:
                return '<span class = "text-success"> Peso Normal</span>'
            else:
                return '<span class = "text-danger"> Abaixo do Peso</span>'
        except ValueError:
            return ""

    def __str__(self):
        """Retorna o texto contendo o nome completo"""

        return self.nome_completo

    class Meta:
        """Meta definition for Paciente."""

        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

class Contato(models.Model):
    """Model definition for Contato."""

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    telefone1 = models.CharField("Telefone", max_length=20)
    telefone2 = models.CharField("Telefone 2", max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)

    class Meta:
        """Meta definition for Contato."""

        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        """Unicode representation of Contato."""
        return str(self.paciente) + " - " + self.nome + " - " + self.telefone1
