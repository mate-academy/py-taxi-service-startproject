# Generated by Django 4.2.7 on 2023-11-12 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'Driver', 'verbose_name_plural': 'Drivers'},
        ),
    ]
