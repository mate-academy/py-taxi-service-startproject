# Generated by Django 4.0.3 on 2022-04-03 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_alter_driver_options_alter_car_model_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
    ]
