# Generated by Django 4.1.7 on 2023-03-22 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='licence_number',
            new_name='license_number',
        ),
    ]