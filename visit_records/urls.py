from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import AppointmentListView, CreateAppointmentView, index

app_name = "visit_records"

urlpatterns = [
    # path("", index, name="index"),
    path("", AppointmentListView.as_view(), name="visit_list"),
    # path("add_appointment/", index, name="add_appointment"),
    path("add_appointment/", CreateAppointmentView.as_view(), name="add_appointment"),
    #     path("diagnosis_search/", DiagnosisSearchView.as_view(), name="diagnosis_search"),
    #     path("doctors/", DoctorsListView.as_view(), name="doctors_list"),
    #     path("doctors_search/", DoctorsSearchView.as_view(), name="doctors_search"),
    #     path("labs/", LaboratoryListView.as_view(), name="laboratory_list"),
    #     path("labs_search/", LaboratorySearchView.as_view(), name="laboratory_search"),
    #     path("clinics/", MedInstitutionListView.as_view(), name="med_inst_list"),
    #     path(
    #         "clinic_detail/<int:pk>",
    #         MedInstitutionDetailView.as_view(),
    #         name="clinic_detail",
    #     ),
    #     path("clinics_search/", MedInstitutionSearchView.as_view(), name="clinic_search"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
