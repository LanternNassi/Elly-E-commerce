# Generated by Django 3.1 on 2020-08-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0002_items_debted_in_items_debted_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items_debted_in',
            name='item',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='items_debted_out',
            name='item',
            field=models.CharField(max_length=12),
        ),
    ]