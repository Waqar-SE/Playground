# Generated by Django 4.1.3 on 2022-11-16 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_auto_20221116_1317"),
    ]

    operations = [
        migrations.CreateModel(
            name="ENumber",
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
                ("number", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
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
                ("name", models.CharField(max_length=20)),
                ("origin", models.CharField(max_length=20)),
                (
                    "is_halal",
                    models.CharField(
                        choices=[
                            ("H", "Halal"),
                            ("N", "Not Halal"),
                            ("C", "Conditional"),
                        ],
                        default="N",
                        max_length=1,
                    ),
                ),
                (
                    "e_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.enumber"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Meal",
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
                ("name", models.CharField(max_length=50)),
                ("ingredients", models.ManyToManyField(to="core.ingredient")),
            ],
        ),
    ]
