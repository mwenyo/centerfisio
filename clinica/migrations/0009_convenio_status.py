# Generated by Django 2.1.7 on 2019-03-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0008_sessao_sessaoestetica_sessaofisioterapia'),
    ]

    operations = [
        migrations.AddField(
            model_name='convenio',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'ATIVO'), (0, 'INATIVO')], default=1),
        ),
    ]
