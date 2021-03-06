# Generated by Django 3.1 on 2020-08-23 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
        ('debts', '0003_auto_20200823_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items_debted_in',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock'),
        ),
        migrations.AlterField(
            model_name='items_debted_out',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock'),
        ),
    ]
