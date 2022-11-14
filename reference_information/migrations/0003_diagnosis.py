# Generated by Django 4.1.3 on 2022-11-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "reference_information",
            "0002_alter_allergy_options_alter_allergy_allergy_type",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Diagnosis",
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
                ("icd_code", models.CharField(max_length=10)),
                ("title", models.CharField(max_length=300)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Diagnoses",
            },
        ),
    ]
