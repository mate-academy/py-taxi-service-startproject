# Generated by Django 4.1.5 on 2023-01-14 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_driver_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="driver",
            old_name="licence_number",
            new_name="license_number",
        ),
    ]
