# Generated by Django 3.1 on 2020-09-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacoes', '0011_agendamentopagamento_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='valor_diferenciado',
            field=models.BooleanField(default=False, verbose_name='Valor Diferenciado'),
        ),
    ]