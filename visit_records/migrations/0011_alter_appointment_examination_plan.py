# Generated by Django 4.1.3 on 2022-11-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reference_information", "0014_doctor"),
        ("visit_records", "0010_alter_appointment_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="examination_plan",
            field=models.ManyToManyField(
                blank=True,
                related_name="appointment_health_tests",
                through="visit_records.AppointmentHealthTest",
                to="reference_information.healthtest",
            ),
        ),
    ]
