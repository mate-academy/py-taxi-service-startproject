# Generated by Django 4.1 on 2023-07-30 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={"ordering": ["model"]},
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={"ordering": ["name"]},
        ),
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="taxi.manufacturer"
            ),
        ),
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
