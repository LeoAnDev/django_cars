# Generated by Django 5.0.7 on 2024-07-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="factory_year",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="car",
            name="model_year",
            field=models.PositiveIntegerField(),
        ),
    ]