# Generated by Django 3.2.6 on 2021-08-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaksiya_app', '0010_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.TextField(),
        ),
    ]