# Generated by Django 4.2.5 on 2024-12-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_aluno2_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=14, null=True, unique=True),
        ),
    ]