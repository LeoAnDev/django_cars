# Generated by Django 5.0.7 on 2024-07-24 19:14

import django.forms.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0002_alter_car_factory_year_alter_car_model_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="status",
            field=models.CharField(
                choices=[
                    ("", "Selecione ..."),
                    ("visivel", "Visível"),
                    ("invisivel", "Invisível"),
                ],
                default=django.forms.fields.NullBooleanField,
                max_length=10,
            ),
        ),
    ]