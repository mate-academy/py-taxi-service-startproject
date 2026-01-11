from django.test import TestCase


# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Manufacturer


class CarAdminSearchAndFilterTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.admin_user = User.objects.create_superuser(
            username="admin",
            password="adminpass123",
            email="admin@example.com",
            license_number="ADMIN-LIC-001",
        )
        self.client.force_login(self.admin_user)

        self.manufacturer_a = Manufacturer.objects.create(name="Toyota", country="Japan")
        self.manufacturer_b = Manufacturer.objects.create(name="BMW", country="Germany")

        self.car_1 = Car.objects.create(model="Camry", manufacturer=self.manufacturer_a)
        self.car_2 = Car.objects.create(model="Corolla", manufacturer=self.manufacturer_a)
        self.car_3 = Car.objects.create(model="X5", manufacturer=self.manufacturer_b)

        self.changelist_url = reverse("admin:taxi_car_changelist")

    def test_car_admin_search_by_model(self):
        # q=... is the admin search query param
        response = self.client.get(self.changelist_url, {"q": "Cam"})
        self.assertEqual(response.status_code, 200)

        # "Camry" should be shown, others should not
        self.assertContains(response, "Camry")
        self.assertNotContains(response, "Corolla")
        self.assertNotContains(response, "X5")

    def test_car_admin_filter_by_manufacturer(self):
        # For ForeignKey filters admin uses: <field_name>__id__exact
        response = self.client.get(
            self.changelist_url,
            {"manufacturer__id__exact": str(self.manufacturer_b.id)},
        )
        self.assertEqual(response.status_code, 200)

        # Only BMW cars should be shown
        self.assertContains(response, "X5")
        self.assertNotContains(response, "Camry")
        self.assertNotContains(response, "Corolla")