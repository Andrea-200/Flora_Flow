# Generated by Django 5.1 on 2024-08-24 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flower",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="flowers/")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="CareTip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tip", models.TextField()),
                (
                    "flower",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="care_tips",
                        to="base.flower",
                    ),
                ),
            ],
        ),
    ]
