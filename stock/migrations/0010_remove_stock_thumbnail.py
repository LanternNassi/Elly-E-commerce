# Generated by Django 3.1 on 2020-10-31 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_auto_20201030_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='thumbnail',
        ),
    ]