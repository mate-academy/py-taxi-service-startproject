# Generated by Django 4.1.3 on 2022-12-01 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['username'], 'verbose_name_plural': 'drivers'},
        ),
    ]
