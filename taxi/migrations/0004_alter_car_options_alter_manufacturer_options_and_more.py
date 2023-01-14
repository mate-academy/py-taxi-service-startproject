# Generated by Django 4.1.5 on 2023-01-14 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0003_rename_licence_number_driver_license_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={"ordering": ["model", "manufacturer"]},
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={"ordering": ["name", "country"]},
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
