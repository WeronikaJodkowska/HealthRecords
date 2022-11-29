from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, DetailView, ListView

from visit_records.forms import (AppointmentDiagnosisFormSet,
                                 AppointmentHealthTestFormSet,
                                 CreateAppointmentForm)
from visit_records.models import (Appointment, AppointmentDiagnosis,
                                  AppointmentHealthTest)


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


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    context_object_name = "appointment"
    template_name = "visit_records/appointment_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["diagnoses"] = AppointmentDiagnosis.objects.filter(
            appointment_id=self.kwargs.get("pk")
        )
        context["health_tests"] = AppointmentHealthTest.objects.filter(
            appointment_id=self.kwargs.get("pk")
        )
        return context


class CreateAppointmentView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = CreateAppointmentForm
    template_name = "visit_records/add_appointment.html"

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
        appointment = self.kwargs.get("pk")
        diagnoses = context["diagnoses"]
        health_tests = context["health_tests"]

        form.instance.user = self.request.user
        # self.object =
        if diagnoses.is_valid() and health_tests.is_valid():
            diagnoses.save()
            health_tests.save()
        form.save()
        return super(CreateAppointmentView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("visit_records:visit_list")
