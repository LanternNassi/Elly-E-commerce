# Generated by Django 3.1 on 2020-08-29 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_stock_overall_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='overall_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
