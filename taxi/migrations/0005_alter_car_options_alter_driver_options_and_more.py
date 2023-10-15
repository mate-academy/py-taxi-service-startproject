# Generated by Django 4.0.2 on 2023-10-15 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_alter_driver_email_alter_driver_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['model', 'manufacturer']},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['first_name', 'last_name', 'username']},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name']},
        ),
    ]
