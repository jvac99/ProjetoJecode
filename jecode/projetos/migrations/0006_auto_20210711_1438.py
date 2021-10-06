# Generated by Django 3.2.2 on 2021-07-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0005_alter_atividade_requisitos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('fazendo', 'Fazendo'), ('feito', 'Feito')], default='pendente', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='titulo',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='lista',
            name='nome',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
