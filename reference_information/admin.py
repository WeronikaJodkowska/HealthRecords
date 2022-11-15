from django.contrib import admin

from .models import Allergy, Diagnosis, DoctorSpecialization, Symptom


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ["icd_code", "title"]


@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(DoctorSpecialization)
class DoctorSpecializationAdmin(admin.ModelAdmin):
    list_display = ["title"]
