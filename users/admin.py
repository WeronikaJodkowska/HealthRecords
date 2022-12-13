from django.contrib import admin
from django import forms
from datetime import date
from django.db import models
from users.models import Profile


class CustomDateWidget(forms.DateInput):
    DATE_INPUT_WIDGET_REQUIRED_FORMAT = "%Y-%m-%d"

    def __init__(self, attrs=None, format=None):
        if attrs is None:
            attrs = {}
        attrs.update(
            {
                "class": "form-control",
                "type": "date",
                "max": date.today(),
                "min": date(1900, 1, 1),
            }
        )
        self.format = format or self.DATE_INPUT_WIDGET_REQUIRED_FORMAT
        super().__init__(attrs, format=self.DATE_INPUT_WIDGET_REQUIRED_FORMAT)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth"]
    formfield_overrides = {
        models.DateField: {"widget": CustomDateWidget},
    }
