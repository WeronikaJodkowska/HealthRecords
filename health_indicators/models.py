from django.db import models
from django.contrib.auth.models import User


class Indicator(models.Model):
    INDICATOR_TYPE_CHOICES = [
        ("0", "Blood pressure"),
        ("1", "Pulse"),
        ("2", "Sugar level"),
        ("3", "Height"),
        ("4", "Weight"),
    ]

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    indicator_type = models.CharField(
        max_length=1, choices=INDICATOR_TYPE_CHOICES, blank=True, null=True
    )
    indicator_date = models.DateField()
    indicator_time = models.TimeField(blank=True, null=True)
    value = models.CharField(max_length=30)
    comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.get_indicator_type_display()
