# Generated by Django 4.1.7 on 2023-02-26 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
    ]
