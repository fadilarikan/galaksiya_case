# Generated by Django 3.2.6 on 2021-08-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaksiya_app', '0003_auto_20210818_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inStock',
            field=models.BooleanField(default=False),
        ),
    ]
