from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import Profile


def validate_password_strength(value):
    """Validates that a password is as least 7 characters long and has at least
    1 digit and 1 letter.
    """
    min_length = 7

    if len(value) < min_length:
        raise ValidationError(
            _("Password must be at least {0} characters " "long.").format(min_length)
        )

    # check for digit
    if not any(char.isdigit() for char in value):
        raise ValidationError(_("Password must contain at least 1 digit."))

    # check for letter
    if not any(char.isalpha() for char in value):
        raise ValidationError(_("Password must contain at least 1 letter."))


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        if validate_password_strength(cd["password"]):
            raise forms.ValidationError("Passwords are too short.")
        return cd["password2"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label="Email")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.TextInput())
    first_name = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput()
    )
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ProfileEditForm(forms.ModelForm):

    BLOOD_TYPE_CHOICES = (
        ("O+", "O+"),
        ("O-", "O-"),
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    )

    GENDER_CHOICES = (
        ("0", "male"),
        ("1", "female"),
        ("2", "other"),
    )

    date_of_birth = forms.DateField(
        required=True, widget=forms.SelectDateWidget(years=range(1900, 2100))
    )
    blood_type = forms.ChoiceField(
        choices=BLOOD_TYPE_CHOICES, required=True, widget=forms.Select()
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, required=True, widget=forms.Select()
    )
    height = forms.CharField(max_length=10, required=True, widget=forms.TextInput())
    weight = forms.CharField(max_length=10, required=True, widget=forms.TextInput())

    class Meta:
        model = Profile
        fields = ("date_of_birth", "blood_type", "gender", "height", "weight")
