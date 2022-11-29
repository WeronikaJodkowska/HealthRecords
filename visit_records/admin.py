from django.contrib import admin
from easy_select2 import select2_modelform

from .models import Appointment, AppointmentDiagnosis

AppointmentForm = select2_modelform(Appointment, attrs={"width": "250px"})


class RecipeIngredientsInline(admin.TabularInline):
    model = AppointmentDiagnosis


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentForm
    list_display = ["med_category", "appointment_date", "status"]
    search_fields = ["diagnosis__icd_code"]
    filter_horizontal = ["examination_plan", "diagnosis"]
    inlines = [RecipeIngredientsInline]


@admin.register(AppointmentDiagnosis)
class AppointmentDiagnosisAdmin(admin.ModelAdmin):
    list_display = ["appointment", "diagnosis"]
