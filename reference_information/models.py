from django.db import models


class Allergy(models.Model):
    class Meta:
        verbose_name_plural = "Allergies"

    ALLERGY_TYPE_CHOICES = [
        ("0", "Household allergy"),
        ("1", "Pollen allergy"),
        ("2", "Animal allergy"),
        ("3", "Fungal allergy"),
        ("4", "Insect allergy"),
        ("5", "Food allergy"),
        ("6", "Drug allergy"),
        ("7", "Industrial allergy"),
    ]

    title = models.CharField(max_length=100)
    allergy_type = models.CharField(
        max_length=1, choices=ALLERGY_TYPE_CHOICES, blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Diagnosis(models.Model):
    class Meta:
        verbose_name_plural = "Diagnoses"

    icd_code = models.CharField(max_length=10)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class DoctorSpecialization(models.Model):
    class Meta:
        verbose_name_plural = "Doctor's specializations"

    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class HealthTest(models.Model):
    class Meta:
        verbose_name_plural = "Health tests"

    test_code = models.CharField(max_length=10, default=0)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class MedInstitution(models.Model):
    class Meta:
        verbose_name_plural = "Med institutions"

    title = models.CharField(max_length=300)
    address_1 = models.CharField(max_length=300)
    address_2 = models.CharField(max_length=300, blank=True, null=True)
    address_3 = models.CharField(max_length=300, blank=True, null=True)
    address_4 = models.CharField(max_length=300, blank=True, null=True)
    address_5 = models.CharField(max_length=300, blank=True, null=True)
    phone_1 = models.CharField(max_length=20, blank=True, null=True)
    phone_2 = models.CharField(max_length=20, blank=True, null=True)
    phone_3 = models.CharField(max_length=20, blank=True, null=True)
    site = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.title


class Laboratory(models.Model):
    class Meta:
        verbose_name_plural = "Laboratories"

    title = models.CharField(max_length=300)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    site = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.title


class MedCategory(models.Model):
    class Meta:
        verbose_name_plural = "Medicine categories"

    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    class Meta:
        verbose_name_plural = "Doctors"

    name = models.CharField(max_length=100)
    speciality = models.ForeignKey(
        DoctorSpecialization,
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        MedCategory, blank=True, null=True, default=None, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Symptom(models.Model):
    class Meta:
        verbose_name_plural = "Symptoms"

    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
