from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, ButtonHolder, Div, Field, Layout, Submit
from django import forms
from easy_select2 import Select2

from health_indicators.models import Indicator


class CreateIndicatorForm(forms.ModelForm):

    INDICATOR_TYPE_CHOICES = [
        ("0", "Blood pressure"),
        ("1", "Pulse"),
        ("2", "Sugar level"),
        ("3", "Height"),
        ("4", "Weight"),
    ]

    indicator_type = forms.ChoiceField(
        choices=INDICATOR_TYPE_CHOICES,
        widget=Select2(attrs={"class": "form-control form-control-sm"}),
    )
    indicator_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2000, 2050))
    )
    indicator_time = forms.TimeField(
        required=False, widget=forms.TimeInput(attrs={"type": "time"})
    )
    value = forms.CharField()
    comment = forms.TextInput()

    class Meta:
        model = Indicator
        fields = "__all__"
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(CreateIndicatorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 create-label"
        self.helper.field_class = "form-control col-md-9"
        self.helper.layout = Layout(
            Div(
                HTML("<br>"),
                Field("indicator_type"),
                HTML("<br>"),
                Field("indicator_date"),
                HTML("<br>"),
                Field("indicator_time"),
                HTML("<br>"),
                Field("value"),
                Field("comment"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "submit")),
            )
        )
