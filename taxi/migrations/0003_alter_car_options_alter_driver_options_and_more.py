# Generated by Django 4.2.7 on 2023-11-12 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_alter_car_manufacturer_alter_manufacturer_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ('model',)},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ('username',)},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ('name',)},
        ),
    ]
