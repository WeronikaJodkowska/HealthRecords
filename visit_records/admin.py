from django.contrib import admin
from easy_select2 import select2_modelform

from .models import Appointment, AppointmentDiagnosis, AppointmentHealthTest

AppointmentForm = select2_modelform(Appointment, attrs={"width": "250px"})


class AppointmentDiagnosisInline(admin.TabularInline):
    model = AppointmentDiagnosis


class AppointmentHealthTestInline(admin.TabularInline):
    model = AppointmentHealthTest


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentForm
    list_display = ["med_category", "appointment_date", "status"]
    search_fields = ["diagnosis__icd_code"]
    filter_horizontal = ["examination_plan", "diagnosis"]
    inlines = [AppointmentDiagnosisInline, AppointmentHealthTestInline]


@admin.register(AppointmentDiagnosis)
class AppointmentDiagnosisAdmin(admin.ModelAdmin):
    list_display = ["appointment", "diagnosis"]


@admin.register(AppointmentHealthTest)
class AppointmentHealthTestAdmin(admin.ModelAdmin):
    list_display = ["appointment", "health_test"]
