# Generated by Django 4.1.7 on 2023-03-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0003_alter_driver_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="driver",
            name="license_number",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
