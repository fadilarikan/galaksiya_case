# Generated by Django 3.2.6 on 2021-08-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaksiya_app', '0019_alter_product_datepublished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datePublished',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
