# Generated by Django 3.1 on 2020-10-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_sales', '0015_auto_20201003_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_items',
            name='Overall_item_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
