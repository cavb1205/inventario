# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-10 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto_imagenproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreColor', models.CharField(max_length=100)),
                ('descripcionColor', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='marcaProducto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.Marca'),
        ),
    ]
