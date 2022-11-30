import calendar
from datetime import date, datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views import generic
from django.views.generic import CreateView, DetailView, ListView

from analyzes_records.models import LabTest
from analyzes_records.utils import Calendar
from analyzes_records.forms import CreateAnalysisForm


class LabTestListView(ListView):
    model = LabTest
    context_object_name = "test_list"
    template_name = "analyzes_records/my_tests.html"
    paginate_by = 10

    def get_queryset(self):
        try:
            entry = LabTest.objects.filter(user=self.request.user)
        except ObjectDoesNotExist:
            print("Either the Appointment or entry doesn't exist.")
        return entry


class LabTestDetailView(LoginRequiredMixin, DetailView):
    model = LabTest
    context_object_name = "test"
    template_name = "analyzes_records/test_detail.html"


class CalendarView(generic.ListView):
    model = LabTest
    template_name = "analyzes_records/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get("month", None))
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        return context


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


class CreateAnalysisView(LoginRequiredMixin, CreateView):
    form_class = CreateAnalysisForm
    template_name = "analyzes_records/add_test.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.is_valid():
            form.save()

        return super(CreateAnalysisView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("analyzes_records:analysis", kwargs={"pk": self.object.pk})
