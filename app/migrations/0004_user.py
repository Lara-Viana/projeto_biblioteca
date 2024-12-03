# Generated by Django 5.1.2 on 2024-11-05 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_autor_nome_alter_editora_nome_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do usuario')),
                ('cpf', models.CharField(max_length=100, verbose_name='CPF')),
                ('data_nasc', models.DateField()),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('telefone', models.IntegerField()),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade do usuario')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
    ]
