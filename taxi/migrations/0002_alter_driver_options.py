# Generated by Django 5.0.1 on 2024-01-06 19:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "Driver", "verbose_name_plural": "Drivers"},
        ),
    ]
