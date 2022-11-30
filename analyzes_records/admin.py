from django.contrib import admin
from easy_select2 import select2_modelform

from .models import LabTest, Test

LabTestForm = select2_modelform(LabTest, attrs={"width": "250px"})
TestForm = select2_modelform(Test, attrs={"width": "250px"})


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    form = LabTestForm
    list_display = ["user", "test_date"]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    form = TestForm
    list_display = ["analysis", "lab_test_id"]
