# Generated by Django 4.1.3 on 2022-11-30 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("health_indicators", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="indicator",
            name="comment",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
