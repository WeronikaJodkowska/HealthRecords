from django.contrib import admin
from easy_select2 import select2_modelform

from .models import Appointment, AppointmentAnalysis, AppointmentDiagnosis

AppointmentForm = select2_modelform(Appointment, attrs={"width": "250px"})


class AppointmentDiagnosisInline(admin.TabularInline):
    model = AppointmentDiagnosis


class AppointmentAnalysisInline(admin.TabularInline):
    model = AppointmentAnalysis


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentForm
    list_display = ["med_category", "appointment_date", "status"]
    search_fields = ["diagnosis__icd_code"]
    filter_horizontal = ["analysis", "diagnosis"]
    inlines = [AppointmentDiagnosisInline, AppointmentAnalysisInline]


@admin.register(AppointmentDiagnosis)
class AppointmentDiagnosisAdmin(admin.ModelAdmin):
    list_display = ["appointment", "diagnosis"]


@admin.register(AppointmentAnalysis)
class AppointmentAnalysisAdmin(admin.ModelAdmin):
    list_display = ["appointment", "analysis"]
