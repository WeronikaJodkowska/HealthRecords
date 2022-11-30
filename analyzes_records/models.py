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

    def __str__(self):
        return self.user.email + " / " + self.lab.title + " / " + str(self.test_date)


class Test(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    result = models.FloatField()
    measurement = models.CharField(max_length=50)
    reference = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    lab_test_id = models.ForeignKey(LabTest, on_delete=models.CASCADE)

    def __str__(self):
        return (
            self.analysis.title
            + " / "
            + self.lab_test_id.lab.title
            + " / "
            + str(self.lab_test_id.test_date)
        )
