# Generated by Django 3.1 on 2020-09-14 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20200902_1049'),
        ('daily_sales', '0006_auto_20200913_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_entry',
            name='product',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='stock.stock'),
        ),
    ]