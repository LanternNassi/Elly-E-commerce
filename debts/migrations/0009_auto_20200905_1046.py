# Generated by Django 3.1 on 2020-09-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0008_auto_20200905_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='debts_in',
            name='situation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='debts_out',
            name='situation',
            field=models.BooleanField(default=False),
        ),
    ]
