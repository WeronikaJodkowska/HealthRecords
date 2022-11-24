from django.contrib import admin

from .models import (Allergy, Diagnosis, Doctor, DoctorSpecialization,
                     HealthTest, Laboratory, MedCategory, MedInstitution,
                     Symptom)


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ["icd_code", "title"]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(DoctorSpecialization)
class DoctorSpecializationAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(HealthTest)
class HealthTestAdmin(admin.ModelAdmin):
    list_display = ["title"]


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
