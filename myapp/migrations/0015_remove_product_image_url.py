# Generated by Django 4.2.6 on 2023-12-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]