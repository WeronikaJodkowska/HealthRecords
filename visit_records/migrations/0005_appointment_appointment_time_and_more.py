# Generated by Django 4.1.3 on 2022-11-28 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visit_records", "0004_appointment_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="appointment_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="appointment_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="file",
            field=models.FileField(
                blank=True, null=True, upload_to="staticfiles/appointment_files"
            ),
        ),
    ]
