# Generated by Django 3.1 on 2020-08-28 18:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacientes', '0001_initial'),
        ('procedimentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField(verbose_name='Horário')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('status', models.SmallIntegerField(choices=[(0, 'A CONFIRMAR'), (1, 'CONFIRMADO'), (2, 'EM ESPERA'), (3, 'EM ATENDIMENTO'), (4, 'ENCERRADO')], default=0, verbose_name='Situação')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
                ('procedimentos', models.ManyToManyField(blank=True, to='procedimentos.Procedimento')),
                ('procedimentos_promo', models.ManyToManyField(blank=True, to='procedimentos.ProcedimentoPromocao', verbose_name='Procedimentos em Promoção')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
            },
        ),
        migrations.CreateModel(
            name='FormaDePagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Descrição')),
                ('acrescimo', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=6, null=True, verbose_name='Acréscimo')),
                ('desconto', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=6, null=True, verbose_name='Desconto')),
            ],
            options={
                'verbose_name': 'Forma de Pagamento',
                'verbose_name_plural': 'Formas de Pagamentos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao', models.SmallIntegerField(choices=[(1, 'ADMINISTRADOR'), (2, 'ESTETICISTA')], default=2, verbose_name='Função')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('abertura', models.TimeField(auto_now_add=datetime.time(18, 44, 13, 486589))),
                ('fechamento', models.TimeField(blank=True, null=True)),
                ('saldo_inicial', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Saldo Inicial')),
                ('saldo', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Saldo')),
                ('status', models.BooleanField(default=1, verbose_name='Aberto')),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacoes.usuario')),
            ],
            options={
                'verbose_name': 'Caixa',
                'verbose_name_plural': 'Caixas',
            },
        ),
        migrations.CreateModel(
            name='AgendamentoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_pago', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Total Pago')),
                ('agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacoes.agendamento')),
                ('caixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacoes.caixa')),
            ],
            options={
                'verbose_name': 'Agendamento Pago',
                'verbose_name_plural': 'Agendamentos Pagos',
            },
        ),
        migrations.CreateModel(
            name='AgendamentoFormasDePagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor Pago')),
                ('agendamento_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacoes.agendamentopago')),
                ('forma_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacoes.formadepagamento')),
            ],
            options={
                'verbose_name': 'Agendamento com Multiplas Formas de Pagamento',
                'verbose_name_plural': 'Agendamentos com Multiplas Formas de Pagamento',
            },
        ),
        migrations.AddField(
            model_name='agendamento',
            name='profisioal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profissional', to='movimentacoes.usuario'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacoes.usuario'),
        ),
    ]
