# Generated by Django 4.2.10 on 2024-02-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
