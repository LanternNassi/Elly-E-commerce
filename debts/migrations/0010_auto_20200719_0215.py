# Generated by Django 3.1 on 2020-07-19 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0009_auto_20200905_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='debts_in',
            name='Balance',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='debts_in',
            name='Paid',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='situation_in',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_paid', models.DateTimeField(auto_created=True)),
                ('Day', models.CharField(max_length=10)),
                ('Amount_paid', models.PositiveIntegerField()),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debts.debts_in')),
            ],
        ),
    ]