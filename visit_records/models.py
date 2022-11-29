from django.contrib.auth.models import User
from django.db import models

from reference_information.models import (Diagnosis, Doctor, HealthTest,
                                          MedCategory, MedInstitution)


class Appointment(models.Model):

    STATUS_CHOICES = [
        ("0", "Scheduled"),
        ("1", "Completed"),
    ]

    class Meta:
        verbose_name_plural = "Appointments"

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    med_category = models.ForeignKey(
        MedCategory, default=None, on_delete=models.CASCADE
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField(blank=True, null=True)
    reminder = models.BooleanField(default=False, help_text="Create a reminder?")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    previous_appointment = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE
    )
    clinic = models.ForeignKey(MedInstitution, default=None, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, default=None, on_delete=models.CASCADE)
    examination_protocol = models.TextField(
        blank=True, null=True, help_text="Patient's complaints"
    )
    conclusion = models.TextField(
        blank=True, null=True, help_text="Diagnoses and health problems"
    )
    diagnosis = models.ManyToManyField(
        Diagnosis,
        blank=False,
        related_name="appointment_diagnoses",
        through="AppointmentDiagnosis",
    )
    examination_plan = models.ManyToManyField(
        HealthTest, blank=True, related_name="appointment_tests"
    )
    recommendations = models.TextField(
        blank=True, null=True, help_text="Treatment recommendations"
    )
    file = models.FileField(
        upload_to="staticfiles/appointment_files", blank=True, null=True
    )

    def __str__(self):
        return (
            self.med_category.title
            + ", "
            + self.doctor.name
            + ", "
            + str(self.appointment_date)
        )


class AppointmentDiagnosis(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
