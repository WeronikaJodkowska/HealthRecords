from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import ListView

from .models import Appointment


class AppointmentListView(ListView):
    model = Appointment
    context_object_name = "appointment_list"
    template_name = "visit_records/my_appointments.html"
    paginate_by = 10

    def get_queryset(self):
        try:
            entry = Appointment.objects.filter(user=self.request.user)
        except ObjectDoesNotExist:
            print("Either the Appointment or entry doesn't exist.")
        return entry


def index(request):
    return render(request, "visit_records/add_appointment.html")
