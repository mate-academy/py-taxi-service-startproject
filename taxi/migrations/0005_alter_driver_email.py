# Generated by Django 5.0.3 on 2024-03-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0004_alter_driver_email_alter_driver_license_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="email",
            field=models.CharField(max_length=99),
        ),
    ]
