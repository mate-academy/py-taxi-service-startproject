# Generated by Django 4.2.5 on 2023-09-11 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0001_initial"),
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
            name="drivers",
            field=models.ManyToManyField(
                related_name="car_drivers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="car_manufacturer",
                to="taxi.manufacturer",
            ),
        ),
    ]
