# Generated by Django 4.2.6 on 2023-10-19 14:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Taxi",
            new_name="Manufacturer",
        ),
    ]
