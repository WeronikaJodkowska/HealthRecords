from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from .models import Diagnosis, Doctor, Laboratory, MedInstitution


def index(request):
    return render(request, "reference_information/index.html")


class DiagnosisListView(ListView):
    model = Diagnosis
    context_object_name = "diagnosis_list"
    template_name = "reference_information/lists/diagnosis.html"
    paginate_by = 50


class DiagnosisSearchView(ListView):
    model = Diagnosis
    template_name = "reference_information/search/diagnosis_search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Diagnosis.objects.filter(
            Q(title__icontains=query) | Q(icd_code__icontains=query)
        )

        if not object_list:
            object_list = Diagnosis.objects.all()

        return object_list


class DoctorsListView(ListView):
    model = Doctor
    context_object_name = "doctors_list"
    template_name = "reference_information/lists/doctors.html"
    paginate_by = 10


class LaboratoryListView(ListView):
    model = Laboratory
    context_object_name = "laboratory_list"
    template_name = "reference_information/lists/laboratories.html"
    paginate_by = 10


class MedInstitutionListView(ListView):
    model = MedInstitution
    context_object_name = "med_inst_list"
    template_name = "reference_information/lists/med_institutions.html"
    paginate_by = 10
