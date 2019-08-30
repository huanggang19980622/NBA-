# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-27 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_auto_20190827_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsimage',
            name='sku',
        ),
        migrations.AddField(
            model_name='goodssku',
            name='images',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shops.GoodsImage', verbose_name='其他图片'),
            preserve_default=False,
        ),
    ]