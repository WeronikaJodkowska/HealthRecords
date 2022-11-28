# Generated by Django 4.1.3 on 2022-11-26 02:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("visit_records", "0003_alter_appointment_previous_appointment"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
