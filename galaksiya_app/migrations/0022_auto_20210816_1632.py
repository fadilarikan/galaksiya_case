# Generated by Django 3.2.6 on 2021-08-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaksiya_app', '0021_alter_product_datepublished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.TextField(),
        ),
    ]