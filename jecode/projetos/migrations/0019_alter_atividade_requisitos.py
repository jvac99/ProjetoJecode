# Generated by Django 3.2.2 on 2021-11-05 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0018_alter_subatividade_atividade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='requisitos',
            field=models.ManyToManyField(blank=True, related_name='_projetos_atividade_requisitos_+', to='projetos.Atividade'),
        ),
    ]
