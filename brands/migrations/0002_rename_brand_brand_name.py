# Generated by Django 5.0.7 on 2024-07-24 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("brands", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="brand",
            old_name="brand",
            new_name="name",
        ),
    ]
