from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from health_indicators.views import IndicatorListView, IndicatorDetailView

app_name = "health_indicators"

urlpatterns = [
    path("", IndicatorListView.as_view(), name="indicator_list"),
    path("indicator/<int:pk>", IndicatorDetailView.as_view(), name="indicator"),
    # path("calendar/", CalendarView.as_view(), name="calendar"),
    # path("analysis/add/", CreateAnalysisView.as_view(), name="add_analysis"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
