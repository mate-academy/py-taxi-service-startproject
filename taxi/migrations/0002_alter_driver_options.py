# Generated by Django 4.2.1 on 2023-05-22 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['username'], 'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
    ]
