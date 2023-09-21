# Generated by Django 4.1.7 on 2023-09-18 15:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_car_drivers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="drivers",
            field=models.ManyToManyField(
                related_name="cars", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
