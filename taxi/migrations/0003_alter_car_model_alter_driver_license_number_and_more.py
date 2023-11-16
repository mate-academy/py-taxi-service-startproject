# Generated by Django 4.2.7 on 2023-11-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0002_alter_driver_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="model",
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.CharField(max_length=75, unique=True),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="country",
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="name",
            field=models.CharField(max_length=65, unique=True),
        ),
    ]
