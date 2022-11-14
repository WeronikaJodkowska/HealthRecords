# Generated by Django 4.1.3 on 2022-11-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "reference_information",
            "0002_alter_allergy_options_alter_allergy_allergy_type",
        ),
        ("users", "0006_alter_profile_allergy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="allergy",
            field=models.ManyToManyField(
                blank=True,
                related_name="user_allergies",
                to="reference_information.allergy",
            ),
        ),
    ]
