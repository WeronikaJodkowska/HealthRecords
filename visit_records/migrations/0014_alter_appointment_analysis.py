# Generated by Django 4.1.3 on 2022-11-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reference_information", "0016_analysis"),
        ("visit_records", "0013_appointmentanalysis_appointment_analysis"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="analysis",
            field=models.ManyToManyField(
                related_name="appointment_analyzes",
                through="visit_records.AppointmentAnalysis",
                to="reference_information.analysis",
            ),
        ),
    ]