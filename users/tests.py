from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_view_url_exists(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("users:index"))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse("users:index"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "dashboard.html")


class UserTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username="test",
            email="test@email.com",
            password="test12345"
        )
        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "test@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
