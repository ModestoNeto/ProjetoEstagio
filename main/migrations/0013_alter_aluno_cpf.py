# Generated by Django 4.2.5 on 2024-12-06 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_aluno_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
