from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('py_taxi_service', '0001_initial'),
    ]
    operations = [
        migrations.AlterModelOptions(
            name='Driver',
            options={'verbose_name': 'Driver', 'verbose_name_plural': 'Drivers'},
        ),
    ]