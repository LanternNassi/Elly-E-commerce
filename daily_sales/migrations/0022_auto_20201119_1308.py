# Generated by Django 3.1 on 2020-11-19 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_sales', '0021_auto_20201119_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_items',
            name='Overall_item_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receipt_items',
            name='Selling_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receipts',
            name='Overall_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
