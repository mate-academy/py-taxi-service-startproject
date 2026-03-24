from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Manufakturer",
            new_name="Manufacturer",
        ),
        migrations.RenameField(
            model_name="car",
            old_name="manufakturer",
            new_name="manufacturer",
        ),
    ]
