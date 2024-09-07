# Generated by Django 5.1.1 on 2024-09-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('cpf_hash', models.CharField(editable=False, max_length=64)),
            ],
        ),
    ]