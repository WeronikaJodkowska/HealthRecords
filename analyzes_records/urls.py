from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from analyzes_records.views import CalendarView, LabTestDetailView, LabTestListView

app_name = "analyzes_records"

urlpatterns = [
    path("", LabTestListView.as_view(), name="test_list"),
    path("calendar/analysis/<int:pk>", LabTestDetailView.as_view(), name="analysis"),
    path("calendar/", CalendarView.as_view(), name="calendar"),
    # path("add_appointment/", CreateAppointmentView.as_view(), name="add_appointment"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
