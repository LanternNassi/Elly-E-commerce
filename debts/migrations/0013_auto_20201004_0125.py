# Generated by Django 3.1 on 2020-10-04 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0012_auto_20200719_0347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='debts_in',
            options={'verbose_name_plural': 'debts in'},
        ),
        migrations.AlterModelOptions(
            name='debts_out',
            options={'verbose_name_plural': 'debts out'},
        ),
    ]
