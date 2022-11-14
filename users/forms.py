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


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        if validate_password_strength(cd["password"]):
            raise forms.ValidationError("Passwords are too short.")
        return cd["password2"]
