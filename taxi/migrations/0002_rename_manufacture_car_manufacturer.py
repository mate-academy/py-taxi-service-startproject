# Generated by Django 5.0.2 on 2024-02-21 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='manufacture',
            new_name='manufacturer',
        ),
    ]
