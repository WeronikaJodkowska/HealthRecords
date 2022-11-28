from django.contrib import admin
from easy_select2 import select2_modelform

from .models import Appointment

AppointmentForm = select2_modelform(Appointment, attrs={"width": "250px"})


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentForm

    list_display = ["med_category", "appointment_date", "status"]
    search_fields = ["diagnosis__icd_code"]
    filter_horizontal = ["examination_plan", "diagnosis"]
