# Generated by Django 4.1.3 on 2022-11-26 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_remove_profile_allergy"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="surname",
        ),
    ]
