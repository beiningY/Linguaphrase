# Generated by Django 4.2.6 on 2024-01-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Word",
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
                ("word", models.CharField(max_length=100)),
                ("definition", models.TextField()),
                ("example", models.TextField()),
                ("image_url", models.URLField()),
            ],
        ),
    ]
