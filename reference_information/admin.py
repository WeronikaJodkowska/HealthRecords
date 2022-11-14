from django.contrib import admin

from .models import Allergy, Diagnosis


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ["icd_code", "title"]
