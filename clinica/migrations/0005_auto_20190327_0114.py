# Generated by Django 2.1.7 on 2019-03-27 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0004_auto_20190327_0111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TipoTratamento',
            new_name='Tipo',
        ),
    ]