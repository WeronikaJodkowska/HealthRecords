# Generated by Django 4.1.3 on 2022-12-13 14:07

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_alter_profile_height_alter_profile_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="date_of_birth",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(
                        datetime.date(2022, 12, 13)
                    ),
                    django.core.validators.MinValueValidator(datetime.date(1900, 1, 1)),
                ],
            ),
        ),
    ]