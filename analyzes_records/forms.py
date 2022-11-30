from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, ButtonHolder, Div, Field, Layout, Submit
from django import forms
from easy_select2 import Select2

from reference_information.models import Analysis, Laboratory
from analyzes_records.models import LabTest


class CreateAnalysisForm(forms.ModelForm):
    lab = forms.ModelChoiceField(
        queryset=Laboratory.objects.all(),
        widget=Select2(attrs={"class": "form-control form-control-sm"}),
    )
    test_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)))
    test_time = forms.TimeField(
        required=False, widget=forms.TimeInput(attrs={"type": "time"})
    )
    previous_test = forms.ModelChoiceField(
        queryset=LabTest.objects.all(),
        required=False,
        widget=Select2(attrs={"class": "form-control form-control-sm"}),
    )
    analysis = forms.ModelChoiceField(
        queryset=Analysis.objects.all(),
        widget=Select2(attrs={"class": "form-control form-control-sm"}),
    )
    result = forms.FloatField()
    measurement = forms.CharField()
    reference = forms.TextInput()
    comment = forms.TextInput()
    file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control form-control-sm"}),
    )

    class Meta:
        model = LabTest
        fields = "__all__"
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(CreateAnalysisForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 create-label"
        self.helper.field_class = "form-control col-md-9"
        self.helper.layout = Layout(
            Div(
                HTML("<br>"),
                Field("lab"),
                Field("test_date"),
                Field("test_time"),
                HTML("<br>"),
                Field("previous_test"),
                Field("analysis"),
                Field("result"),
                HTML("<br>"),
                Field("measurement"),
                Field("reference"),
                HTML("<br>"),
                Field("comment"),
                Field("file"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "submit")),
            )
        )
