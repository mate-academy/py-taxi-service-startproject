# Generated by Django 4.0.5 on 2022-06-28 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_car_manufacturer_alter_manufacturer_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "driver", "verbose_name_plural": "drivers"},
        ),
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.CharField(max_length=200),
        ),
    ]
