from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, ButtonHolder, Div, Field, Fieldset,
                                 Layout, Submit)
from django import forms
from django.forms.models import inlineformset_factory
from easy_select2 import Select2, Select2Multiple

from reference_information.models import (Diagnosis, Doctor, MedCategory,
                                          MedInstitution)
from visit_records.custom_layout_object import Formset
from visit_records.models import Appointment, AppointmentDiagnosis


class CreateAppointmentForm(forms.ModelForm):
    STATUS_CHOICES = [
        ("0", "Scheduled"),
        ("1", "Completed"),
    ]

    med_category = forms.ModelChoiceField(
        queryset=MedCategory.objects.all(),
        widget=Select2(attrs={"class": "form-control form-control-sm"}),
    )
    appointment_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2000, 2050))
    )
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    reminder = forms.CheckboxInput()
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect)
    previous_appointment = forms.ModelChoiceField(
        queryset=Appointment.objects.all(),
        widget=Select2(attrs={"class": "form-control form-control-sm"}),
    )
    clinic = forms.ModelChoiceField(
        queryset=MedInstitution.objects.all(),
        widget=Select2(attrs={"class": "form-control form-control-sm"}),
    )
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        widget=Select2(attrs={"class": "form-control form-control-sm"}),
    )
    examination_protocol = forms.TextInput()
    conclusion = forms.TextInput()
    # diagnosis = forms.ModelMultipleChoiceField(queryset=Diagnosis.objects.all(),
    #                                            widget=Select2Multiple(select2attrs={"class": "form-control form-control-sm"}))

    class Meta:
        model = Appointment
        fields = "__all__"
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        self.fields["med_category"].label = "Category"

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 create-label"
        self.helper.field_class = "form-control col-md-9"
        self.helper.layout = Layout(
            Div(
                HTML("<br>"),
                Field("med_category"),
                Field("appointment_date"),
                Field("appointment_time"),
                HTML("<br>"),
                Field("reminder"),
                Field("status"),
                Field("previous_appointment"),
                Field("clinic"),
                Field("doctor"),
                HTML("<br>"),
                Field("examination_protocol"),
                Field("conclusion"),
                HTML("<br>"),
                Fieldset("Diagnoses", Formset("diagnoses")),
                HTML("<br>"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
            )
        )


class AppointmentDiagnosisForm(forms.ModelForm):
    class Meta:
        model = AppointmentDiagnosis
        exclude = ()


AppointmentDiagnosisFormSet = inlineformset_factory(
    Appointment,
    AppointmentDiagnosis,
    form=AppointmentDiagnosisForm,
    fields="__all__",
    extra=3,
    can_delete=True,
    widgets={
        "diagnosis": forms.Select(attrs={"class": "form-control form-control-sm"}),
    },
)
