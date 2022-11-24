from django.shortcuts import render
from django.views.generic import ListView

from .models import Doctor


def index(request):
    return render(request, "reference_information/index.html")


class DoctorsListView(ListView):
    model = Doctor
    context_object_name = "doctors_list"
    template_name = "reference_information/lists/doctors.html"
    paginate_by = 10
