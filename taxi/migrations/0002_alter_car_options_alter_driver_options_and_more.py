# Generated by Django 5.0 on 2024-01-01 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ('manufacturer',)},
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