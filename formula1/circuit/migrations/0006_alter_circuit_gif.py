# Generated by Django 5.0.2 on 2024-02-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuit', '0005_circuit_gif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circuit',
            name='gif',
            field=models.FileField(null=True, upload_to='media/static/gif'),
        ),
    ]