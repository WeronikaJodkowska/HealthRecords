# Generated by Django 4.1.3 on 2022-11-30 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "analyzes_records",
            "0002_labtest_analysis_labtest_comment_labtest_measurement_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="labtest",
            name="file",
            field=models.FileField(
                blank=True, null=True, upload_to="analyzes_files/%Y/%m/%d"
            ),
        ),
    ]