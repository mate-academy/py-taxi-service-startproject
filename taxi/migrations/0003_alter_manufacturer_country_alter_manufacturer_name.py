# Generated by Django 4.2.7 on 2023-11-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0002_alter_driver_email_alter_driver_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manufacturer",
            name="country",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
