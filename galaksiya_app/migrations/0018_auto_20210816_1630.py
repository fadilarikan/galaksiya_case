# Generated by Django 3.2.6 on 2021-08-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaksiya_app', '0017_product_datepublished'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.TextField(default=None),
        ),
    ]
