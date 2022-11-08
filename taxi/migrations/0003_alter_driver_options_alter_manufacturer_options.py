# Generated by Django 4.1.3 on 2022-11-08 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_manufacturer_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={
                "ordering": ["username"],
                "verbose_name": "Driver",
                "verbose_name_plural": "Drivers",
            },
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={"ordering": ["name"]},
        ),
    ]
