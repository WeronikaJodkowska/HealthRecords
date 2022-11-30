from django.contrib.auth.models import User
from django.db import models

from reference_information.models import Analysis, Laboratory


class LabTest(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    lab = models.ForeignKey(Laboratory, default=None, on_delete=models.CASCADE)
    test_date = models.DateField()
    test_time = models.TimeField(blank=True, null=True)
    previous_test = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE
    )
    analysis = models.ForeignKey(Analysis, default=None, on_delete=models.CASCADE)
    result = models.FloatField(default=0.0)
    measurement = models.CharField(max_length=50, default="")
    reference = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="analyzes_files/%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return (
            self.analysis.title + " / " + self.lab.title + " / " + str(self.test_date)
        )
