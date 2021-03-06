# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='quantity',
            new_name='item_quantity',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='unit',
            new_name='item_unit',
        ),
        migrations.RemoveField(
            model_name='products',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='model',
        ),
        migrations.RemoveField(
            model_name='products',
            name='name',
        ),
        migrations.RemoveField(
            model_name='products',
            name='warehouse',
        ),
        migrations.AddField(
            model_name='item',
            name='orginal_price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=12),
        ),
        migrations.AddField(
            model_name='item',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=12),
        ),
        migrations.AddField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=12),
        ),
        migrations.AddField(
            model_name='products',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Item'),
        ),
        migrations.AddField(
            model_name='products',
            name='tax',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=12),
        ),
        migrations.AddField(
            model_name='warehousemanager',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.WareHouse'),
        ),
    ]
