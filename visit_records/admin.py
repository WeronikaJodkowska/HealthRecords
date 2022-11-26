from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["med_category", "appointment_date", "status"]
    search_fields = ["diagnosis__icd_code"]
    filter_horizontal = ["examination_plan", "diagnosis"]
