# Generated by Django 4.0.2 on 2023-12-01 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_alter_driver_options_car_delf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='delf',
        ),
    ]
