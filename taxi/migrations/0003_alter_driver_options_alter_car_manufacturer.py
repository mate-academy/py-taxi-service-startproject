# Generated by Django 4.2.1 on 2023-05-08 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0002_rename_county_manufacturer_country"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={
                "ordering": ("username",),
                "verbose_name": "driver",
                "verbose_name_plural": "drivers",
            },
        ),
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cars",
                to="taxi.manufacturer",
            ),
        ),
    ]