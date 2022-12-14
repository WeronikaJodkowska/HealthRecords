from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .forms import LoginForm, ProfileEditForm, RegisterForm, UpdateUserForm
from .services import create_user


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = "users/change_password.html"
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy("users:edit_profile")


def index(request):
    return render(request, "dashboard.html")


def contact(request):
    return render(request, "contact.html")


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


def register(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            create_user(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            return redirect("users:login_user")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            # if request.user.last_login.time request.user.date_joined.time:
            #     return redirect("users:edit_profile")
            # else:
            return redirect("/")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def edit_profile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "users/profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
