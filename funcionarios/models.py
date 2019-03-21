"""Aplicativo Funcionarios"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Funcionario(models.Model):
    """Model definition for Funcionario."""

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
        ('TO', 'Tocantins')
    )

    ESTADO_CIVIL_CHOICES = (
        ('Solteiro(a)', 'Solteiro(a)'),
        ('Casado(a)', 'Casado(a)'),
        ('Divorciado(a)', 'Divorciado(a)'),
        ('Viúvo(a)', 'Viúvo(a)'),
        ('Amancebado(a)', 'Amancebado(a)'),
    )

    GENERO_CHOICE = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
        ('nd', 'Não declarado')
    )

    usuario = models.OneToOneField(User, verbose_name="Funcionário", \
        on_delete=models.CASCADE, unique=True)
    cpf = models.CharField("CPF", max_length=14, null=False)
    nascimento = models.DateField("Data de nascimento", null=False)
    contratacao = models.DateField("Data de contratação", null=False)
    telefone1 = models.CharField("Telefone", max_length=20, null=False)
    telefone2 = models.CharField("Telefone 2", max_length=20, null=True, blank=True)
    endereco = models.CharField("Endereço", max_length=200, null=True, blank=True)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    numero = models.PositiveSmallIntegerField("Número", null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    uf = models.CharField('Estado', choices=UF_CHOICES, max_length=2,\
        null=True, blank=True)
    estado_civil = models.CharField("Estado civíl", choices=ESTADO_CIVIL_CHOICES, \
        max_length=50, null=True, blank=True)
    genero = models.CharField("Gênero", choices=GENERO_CHOICE, max_length=2,\
        null=True, blank=True)
    foto = models.FileField(upload_to='avatars', null=False)

    class Meta:
        """Meta definition for Funcionario."""

        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    @property
    def full_name(self):
        """Retorna o nome completo do funcionário"""

        return "%s %s" % (self.usuario.first_name, self.usuario.last_name)

    def __str__(self):
        """Retorna o texto contendo o nome completo"""

        return self.full_name

class Fisioterapeuta(models.Model):
    """Model definition for Fisioterapeuta."""

    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    crefito = models.CharField("CREFITO", max_length=50)
    especializacao = models.TextField(null=True, blank=True)
    cursos = models.TextField(null=True, blank=True)

    class Meta:
        """Meta definition for Fisioterapeuta."""

        verbose_name = 'Fisioterapeuta'
        verbose_name_plural = 'Fisioterapeutas'

    def __str__(self):
        """Unicode representation of Fisioterapeuta."""

        if self.funcionario.genero == "f":
            return "Dra. %s" % self.funcionario.full_name

        return "Dr. %s" % self.funcionario.full_name

class Esteticista(models.Model):
    """Model definition for Esteticista."""

    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cursos = models.TextField(null=True, blank=True)

    class Meta:
        """Meta definition for Esteticista."""

        verbose_name = 'Esteticista'
        verbose_name_plural = 'Esteticistas'

    def __str__(self):
        """Unicode representation of Esteticista."""

        return self.funcionario.full_name

class Instrutor(models.Model):
    """Model definition for Instrutor."""

    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    registro = models.CharField("CREFITO/CREF", max_length=50)
    cursos = models.TextField(null=True, blank=True)

    class Meta:
        """Meta definition for Instrutor."""

        verbose_name = 'Instrutor de Pilates'
        verbose_name_plural = 'Instrutores de Pilates'

    def __str__(self):
        """Unicode representation of Instrutor de Pilates."""

        return self.funcionario.full_name
