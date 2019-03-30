# Generated by Django 2.1.7 on 2019-03-27 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_paciente_profissao'),
        ('funcionarios', '0017_administrador'),
        ('clinica', '0002_pacote_procedimentos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Convênio',
                'verbose_name_plural': 'Convênios',
            },
        ),
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='Data Cadastro')),
                ('queixa', models.TextField()),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'ATIVO'), (0, 'INATIVO')], default=1)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.Administrador')),
                ('convenio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Convenio')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente')),
            ],
            options={
                'verbose_name': 'Prontuário',
                'verbose_name_plural': 'Prontuários',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Tipo de tratamento')),
            ],
            options={
                'verbose_name': 'Tipo de Tratamento',
                'verbose_name_plural': 'Tipos de Tratamentos',
            },
        ),
        migrations.AlterField(
            model_name='pacote',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Tipo'),
        ),
        migrations.AlterField(
            model_name='procedimento',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Tipo'),
        ),
        migrations.DeleteModel(
            name='TipoTratamento',
        ),
        migrations.AddField(
            model_name='prontuario',
            name='pacote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Pacote'),
        ),
        migrations.AddField(
            model_name='prontuario',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Tipo'),
        ),
    ]