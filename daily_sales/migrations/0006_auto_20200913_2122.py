# Generated by Django 3.1 on 2020-09-14 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20200902_1049'),
        ('daily_sales', '0005_auto_20200913_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_entry',
            name='Quantity',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='product_entry',
            name='product',
            field=models.ForeignKey(default='sockets', on_delete=django.db.models.deletion.CASCADE, to='stock.stock'),
        ),
    ]