# Generated by Django 3.1 on 2020-07-16 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20200902_1049'),
        ('daily_sales', '0007_auto_20200913_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_entry',
            name='Quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_entry',
            name='Selling_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_entry',
            name='Total_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_entry',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock'),
        ),
    ]
