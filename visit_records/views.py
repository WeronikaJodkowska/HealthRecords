from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from visit_records.forms import (AppointmentDiagnosisFormSet,
                                 AppointmentHealthTestFormSet,
                                 CreateAppointmentForm)
from visit_records.models import Appointment


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


class CreateAppointmentView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = CreateAppointmentForm
    template_name = "visit_records/add_appointment.html"
    success_message = "Appointment added!"

    def get_context_data(self, **kwargs):
        context = super(CreateAppointmentView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["diagnoses"] = AppointmentDiagnosisFormSet(self.request.POST)
            context["health_tests"] = AppointmentHealthTestFormSet(self.request.POST)
        else:
            context["diagnoses"] = AppointmentDiagnosisFormSet()
            context["health_tests"] = AppointmentHealthTestFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        return super(CreateAppointmentView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data
