# Generated by Django 4.1.7 on 2023-02-27 11:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "driver", "verbose_name_plural": "drivers"},
        ),
    ]
