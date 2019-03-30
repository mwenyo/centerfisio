# Generated by Django 2.1.7 on 2019-03-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0017_administrador'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrutor',
            name='conselho',
            field=models.CharField(choices=[('CREFITO', 'CREFITO'), ('CREF', 'CREF')], default='CREFITO', max_length=7, verbose_name='Concelho de Classe'),
        ),
        migrations.AlterField(
            model_name='instrutor',
            name='registro',
            field=models.CharField(max_length=50),
        ),
    ]