# -*- coding: utf-8 -*-

# Generated by Django 1.9.6 on 2016-06-08 19:55



>>>>>>> cec504e3b4041c03724bd18d913bb8cc85d65866
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Billetera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=4)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('actual', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidad', models.PositiveIntegerField()),
                ('ocupada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to=None)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_ini', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rif', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('hora_apertura', models.TimeField()),
                ('hora_cierre', models.TimeField()),
                ('capacidad_max', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to=None)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('rif', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('tipo_usuario', models.CharField(choices=[('A', 'Administrador'), ('C', 'Cliente'), ('P', 'Proveedor')], max_length=1)),
                ('fecha_nac', models.DateField()),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telf', models.CharField(blank=True, max_length=20, null=True)),
                ('billetera', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Billetera')),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='servicio',
            name='provedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Usuario'),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Usuario'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Usuario'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='mesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Mesa'),
        ),
        migrations.AddField(
            model_name='producto',
            name='restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Restaurante'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(to='pedidos.Producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Restaurante'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Usuario'),
        ),
        migrations.AddField(
            model_name='mesa',
            name='restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Restaurante'),
        ),
        migrations.AddField(
            model_name='menu',
            name='productos',
            field=models.ManyToManyField(to='pedidos.Producto'),
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Restaurante'),
        ),
    ]
