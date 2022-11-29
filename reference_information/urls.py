from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from reference_information.views import (DiagnosisListView,
                                         DiagnosisSearchView, DoctorsListView,
                                         DoctorsSearchView, LaboratoryListView,
                                         LaboratorySearchView,
                                         MedInstitutionDetailView,
                                         MedInstitutionListView,
                                         MedInstitutionSearchView, index)

app_name = "reference_information"

urlpatterns = [
    path("", index, name="index"),
    path("diagnoses/", DiagnosisListView.as_view(), name="diagnosis_list"),
    path("diagnosis_search/", DiagnosisSearchView.as_view(), name="diagnosis_search"),
    path("doctors/", DoctorsListView.as_view(), name="doctors_list"),
    path("doctors_search/", DoctorsSearchView.as_view(), name="doctors_search"),
    path("labs/", LaboratoryListView.as_view(), name="laboratory_list"),
    path("labs_search/", LaboratorySearchView.as_view(), name="laboratory_search"),
    path("clinics/", MedInstitutionListView.as_view(), name="med_inst_list"),
    path(
        "clinic/<int:pk>",
        MedInstitutionDetailView.as_view(),
        name="clinic_detail",
    ),
    path("clinics_search/", MedInstitutionSearchView.as_view(), name="clinic_search"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
