# Generated by Django 4.1.3 on 2022-11-29 23:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("reference_information", "0017_alter_analysis_test_code"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LabTest",
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
                ("test_date", models.DateField()),
                ("test_time", models.TimeField(blank=True, null=True)),
                (
                    "lab",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reference_information.laboratory",
                    ),
                ),
                (
                    "previous_test",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="analyzes_records.labtest",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Test",
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
                ("result", models.FloatField()),
                ("measurement", models.CharField(max_length=50)),
                ("reference", models.TextField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "analysis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reference_information.analysis",
                    ),
                ),
                (
                    "lab_test_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="analyzes_records.labtest",
                    ),
                ),
            ],
        ),
    ]