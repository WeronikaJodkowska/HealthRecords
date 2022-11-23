from django.contrib.auth.models import User


def create_user(email: str, username: str, password: str):
    user = User(
        email=email,
        username=username,
    )
    user.set_password(password)
    user.save()
