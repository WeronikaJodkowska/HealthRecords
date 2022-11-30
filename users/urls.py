"""HealthRecords URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users.views import (
    ChangePasswordView,
    contact,
    edit_profile,
    index,
    login_user,
    logout_view,
    register,
)

app_name = "users"

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_view, name="logout"),
    path("profile/", edit_profile, name="edit_profile"),
    path("change_password/", ChangePasswordView.as_view(), name="password_change"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
