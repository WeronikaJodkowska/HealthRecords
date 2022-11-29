from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (AppointmentDetailView, AppointmentListView,
                    CreateAppointmentView)

app_name = "visit_records"

urlpatterns = [
    path("", AppointmentListView.as_view(), name="visit_list"),
    path("appointment/<int:pk>", AppointmentDetailView.as_view(), name="appointment"),
    path("add_appointment/", CreateAppointmentView.as_view(), name="add_appointment"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
