# Generated by Django 3.2.9 on 2022-01-27 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='nome_completo',
            field=models.CharField(max_length=255, verbose_name='Nome completo'),
        ),
    ]
