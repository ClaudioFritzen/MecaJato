# Generated by Django 4.1.1 on 2022-09-22 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('cpf', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carros', models.CharField(max_length=20)),
                ('placas', models.CharField(max_length=20)),
                ('ano', models.CharField(max_length=10)),
                ('lavagens', models.IntegerField(default=0)),
                ('consertos', models.IntegerField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
        ),
    ]