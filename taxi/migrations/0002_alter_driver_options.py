# Generated by Django 4.1.1 on 2022-09-29 10:01

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
