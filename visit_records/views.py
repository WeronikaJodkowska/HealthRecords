from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from visit_records.forms import (AppointmentAnalysisFormSet,
                                 AppointmentDiagnosisFormSet,
                                 CreateAppointmentForm)
from visit_records.models import (Appointment, AppointmentAnalysis,
                                  AppointmentDiagnosis)


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
        ).distinct("diagnosis__title")
        context["analyzes"] = AppointmentAnalysis.objects.filter(
            appointment_id=self.kwargs.get("pk")
        ).distinct("analysis__title")
        return context


class CreateAppointmentView(LoginRequiredMixin, CreateView):
    form_class = CreateAppointmentForm
    template_name = "visit_records/add_appointment.html"

    def get_context_data(self, **kwargs):
        context = super(CreateAppointmentView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["diagnoses"] = AppointmentDiagnosisFormSet(self.request.POST)
            context["analyzes"] = AppointmentAnalysisFormSet(self.request.POST)
        else:
            context["diagnoses"] = AppointmentDiagnosisFormSet()
            context["analyzes"] = AppointmentAnalysisFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        appointment = self.kwargs.get("pk")
        diagnoses = context["diagnoses"]
        analyzes = context["analyzes"]

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if diagnoses.is_valid():
                diagnoses.instance = self.object
                diagnoses.save()
            if analyzes.is_valid():
                analyzes.instance = self.object
                analyzes.save()
        return super(CreateAppointmentView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("visit_records:appointment", kwargs={"pk": self.object.pk})
