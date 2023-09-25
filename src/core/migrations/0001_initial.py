# Generated by Django 4.2 on 2023-09-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StarWarsData",
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
                ("filename", models.CharField()),
                ("data", models.JSONField()),
                ("download_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]