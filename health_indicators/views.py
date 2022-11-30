from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.template.defaultfilters import register
from django.views.generic import CreateView, DetailView, ListView

from health_indicators.models import Indicator


class IndicatorListView(ListView):
    model = Indicator
    context_object_name = "indicators_list"
    template_name = "health_indicators/my_indicators.html"
    paginate_by = 10

    def get_queryset(self):
        try:
            entry = Indicator.objects.filter(user=self.request.user)
        except ObjectDoesNotExist:
            print("Either the Appointment or entry doesn't exist.")
        return entry


class IndicatorDetailView(LoginRequiredMixin, DetailView):
    model = Indicator
    context_object_name = "indicator"
    template_name = "health_indicators/indicator_detail.html"
