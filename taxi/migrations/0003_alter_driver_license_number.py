# Generated by Django 4.1.7 on 2023-03-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_alter_driver_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='license_number',
            field=models.CharField(max_length=63, unique=True),
        ),
    ]
