# Generated by Django 4.1.5 on 2023-01-17 05:38

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
