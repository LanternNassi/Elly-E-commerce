# Generated by Django 3.1 on 2020-10-30 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20200902_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='product-images')),
                ('thumbnail', models.ImageField(null=True, upload_to='product-thumbs')),
                ('Item_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
            ],
        ),
    ]
