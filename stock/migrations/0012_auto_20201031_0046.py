# Generated by Django 3.1 on 2020-10-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_stock_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product-images'),
        ),
    ]
