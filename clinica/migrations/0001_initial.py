# Generated by Django 2.1.7 on 2019-03-27 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('valor', models.FloatField(default=0)),
                ('promocao', models.BooleanField(default=False, verbose_name='Promoção')),
                ('inicio', models.DateField(blank=True, null=True, verbose_name='Data Inicial')),
                ('termino', models.DateField(blank=True, null=True, verbose_name='Data Final')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'ATIVO'), (0, 'INATIVO')])),
            ],
        ),
        migrations.CreateModel(
            name='PacoteProcedimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pacote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Pacote')),
            ],
            options={
                'verbose_name': 'Pacote de procedimentos',
                'verbose_name_plural': 'Pacotes de Procedimentos',
            },
        ),
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('valor_unitario', models.FloatField(default=0.0, verbose_name='Valor Unitário')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'ATIVO'), (0, 'INATIVO')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TipoTratamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do tratamento')),
            ],
            options={
                'verbose_name': 'Tipo de Tratamento',
                'verbose_name_plural': 'Tipos de Tratamentos',
            },
        ),
        migrations.AddField(
            model_name='procedimento',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.TipoTratamento'),
        ),
        migrations.AddField(
            model_name='pacoteprocedimento',
            name='procedimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Procedimento'),
        ),
        migrations.AddField(
            model_name='pacote',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.TipoTratamento'),
        ),
    ]