from django.db import models


class Allergy(models.Model):
    class Meta:
        verbose_name_plural = "Allergies"

    ALLERGY_TYPE_CHOICES = [
        ('0', 'Household allergy'),
        ('1', 'Pollen allergy'),
        ('2', 'Animal allergy'),
        ('3', 'Fungal allergy'),
        ('4', 'Insect allergy'),
        ('5', 'Food allergy'),
        ('6', 'Drug allergy'),
        ('7', 'Industrial allergy'),
    ]

    title = models.CharField(max_length=100)
    allergy_type = models.CharField(max_length=1, choices=ALLERGY_TYPE_CHOICES,
                                    blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
