# Generated by Django 3.1 on 2020-09-02 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_stock_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='image',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='thumbnail',
        ),
    ]
