# Generated by Django 4.2.5 on 2024-12-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_aluno_serie_alter_aluno_turma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='serie',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='turma',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
