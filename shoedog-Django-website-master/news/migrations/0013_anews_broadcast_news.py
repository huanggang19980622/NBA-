# Generated by Django 2.0 on 2018-05-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20180507_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='anews',
            name='broadcast_news',
            field=models.BooleanField(default=False),
        ),
    ]