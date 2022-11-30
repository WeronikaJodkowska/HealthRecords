from django.contrib import admin
from easy_select2 import select2_modelform

from .models import (
    Allergy,
    Analysis,
    Diagnosis,
    Doctor,
    DoctorSpecialization,
    Laboratory,
    MedCategory,
    MedInstitution,
    Symptom,
)

DoctorForm = select2_modelform(Doctor, attrs={"width": "250px"})


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ["icd_code", "title"]
    search_fields = ["icd_code", "title"]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    form = DoctorForm
    list_display = ["name", "speciality"]


@admin.register(DoctorSpecialization)
class DoctorSpecializationAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Analysis)
class HealthTestAdmin(admin.ModelAdmin):
    list_display = ["test_code", "title"]


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(MedCategory)
class MedCategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(MedInstitution)
class MedInstitutionAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ["title"]
