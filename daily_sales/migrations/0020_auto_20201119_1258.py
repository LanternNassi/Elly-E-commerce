# Generated by Django 3.1 on 2020-11-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_sales', '0019_auto_20201108_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipts',
            name='Overall_price',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
    ]
