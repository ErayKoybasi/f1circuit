# Generated by Django 5.0.2 on 2024-02-25 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circuit', '0002_rename_product_circuit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='circuit',
            old_name='circuitName',
            new_name='name',
        ),
    ]