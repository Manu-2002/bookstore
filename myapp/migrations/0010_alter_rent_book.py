# Generated by Django 4.2.6 on 2023-12-04 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_fine_amount_remove_fine_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product'),
        ),
    ]