from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from reference_information.views import (DiagnosisListView,
                                         DiagnosisSearchView, DoctorsListView,
                                         DoctorsSearchView, LaboratoryListView,
                                         MedInstitutionListView, index)

app_name = "reference_information"

urlpatterns = [
    path("", index, name="index"),
    path("diagnoses/", DiagnosisListView.as_view(), name="diagnosis_list"),
    path("diagnosis_search/", DiagnosisSearchView.as_view(), name="diagnosis_search"),
    path("doctors/", DoctorsListView.as_view(), name="doctors_list"),
    path("doctors_search/", DoctorsSearchView.as_view(), name="doctors_search"),
    path("labs/", LaboratoryListView.as_view(), name="laboratory_list"),
    path("clinics/", MedInstitutionListView.as_view(), name="med_inst_list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
