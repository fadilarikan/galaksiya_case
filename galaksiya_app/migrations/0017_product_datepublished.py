# Generated by Django 3.2.6 on 2021-08-16 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galaksiya_app', '0016_remove_product_datepublished'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='datePublished',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
