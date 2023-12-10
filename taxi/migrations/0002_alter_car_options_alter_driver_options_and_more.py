# Generated by Django 5.0 on 2023-12-10 03:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={"ordering": ("model",)},
        ),
        migrations.AlterModelOptions(
            name="driver",
            options={"ordering": ("username",)},
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={"ordering": ("name",)},
        ),
    ]
