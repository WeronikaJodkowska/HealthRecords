# Generated by Django 4.1.3 on 2022-11-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_profile_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="height",
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="weight",
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
    ]