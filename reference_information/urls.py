from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from reference_information.views import DoctorsListView, index

app_name = "reference_information"

urlpatterns = [
    path("", index, name="index"),
    path("doctors/", DoctorsListView.as_view(), name="doctors_list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
