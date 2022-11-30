from django.contrib import admin

from health_indicators.models import Indicator


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ["get_indicator_type_display", "indicator_type"]
