# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='billetera',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Billetera'),
        ),
    ]
