from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from health_indicators.views import IndicatorListView, IndicatorDetailView, CreateIndicatorView

app_name = "health_indicators"

urlpatterns = [
    path("", IndicatorListView.as_view(), name="indicator_list"),
    path("indicator/<int:pk>", IndicatorDetailView.as_view(), name="indicator"),
    # path("calendar/", CalendarView.as_view(), name="calendar"),
    path("indicator/add/", CreateIndicatorView.as_view(), name="add_indicator"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
