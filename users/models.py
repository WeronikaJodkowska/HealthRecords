from django.contrib.auth.models import User
from django.db import models
from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    BLOOD_TYPE_CHOICES = [
        ("O+", "O+"),
        ("O-", "O-"),
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    ]

    GENDER_CHOICES = [
        ("0", "male"),
        ("1", "female"),
        ("2", "other"),
    ]

    TRUE_FALSE_CHOICES = ((True, "Yes"), (False, "No"))

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Username",
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(date.today()),
            MinValueValidator(date(1900, 1, 1)),
        ],
    )
    blood_type = models.CharField(
        max_length=3, choices=BLOOD_TYPE_CHOICES, blank=True, null=True
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True
    )
    height = models.IntegerField(
        blank=True,
        null=True,
        help_text="in cm",
        validators=[MaxValueValidator(300), MinValueValidator(40)],
    )
    weight = models.IntegerField(
        blank=True,
        null=True,
        help_text="in kg",
        validators=[MaxValueValidator(650), MinValueValidator(2)],
    )

    def __str__(self):
        return f"Profile for user {self.user.username}"
