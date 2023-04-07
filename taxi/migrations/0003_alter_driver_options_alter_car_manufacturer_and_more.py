# Generated by Django 4.2 on 2023-04-06 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0002_remove_car_license_plate"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "driver", "verbose_name_plural": "drivers"},
        ),
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="taxi.manufacturer"
            ),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="name",
            field=models.CharField(max_length=63, unique=True),
        ),
    ]
