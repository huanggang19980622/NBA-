# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-27 05:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_auto_20190827_1334'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OtherImage',
        ),
        migrations.AddField(
            model_name='goodsimage',
            name='sku',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shops.GoodsSKU', verbose_name='商品'),
            preserve_default=False,
        ),
    ]