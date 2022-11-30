# Generated by Django 4.1.3 on 2022-11-30 03:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reference_information", "0017_alter_analysis_test_code"),
        ("analyzes_records", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="labtest",
            name="analysis",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="reference_information.analysis",
            ),
        ),
        migrations.AddField(
            model_name="labtest",
            name="comment",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="labtest",
            name="measurement",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="labtest",
            name="reference",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="labtest",
            name="result",
            field=models.FloatField(default=0.0),
        ),
        migrations.DeleteModel(
            name="Test",
        ),
    ]
