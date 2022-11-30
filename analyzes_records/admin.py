from django.contrib import admin
from easy_select2 import select2_modelform

from .models import LabTest

LabTestForm = select2_modelform(LabTest, attrs={"width": "350px"})


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    form = LabTestForm
    list_display = ["user", "lab", "test_date"]
