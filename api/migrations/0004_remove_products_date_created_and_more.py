# Generated by Django 4.0.1 on 2022-03-25 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_products_imagepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='products',
            name='last_modified',
        ),
    ]
