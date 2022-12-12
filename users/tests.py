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
