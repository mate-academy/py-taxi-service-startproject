# Generated by Django 5.0 on 2023-12-06 21:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.IntegerField(unique=True),
        ),
    ]
