# Generated by Django 4.1.3 on 2022-11-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_height_alter_profile_weight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="height",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="weight",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]