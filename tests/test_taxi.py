from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
import os.path

from taxi.models import Manufacturer, Car, Driver


class AdminSiteDriverTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user",
            password="1qazcde3",
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username="test.user",
            password="2wsxvfr4",
            license_number="TES12345"
        )

    def test_license_number_in_driver_changelist(self):
        url = reverse("admin:taxi_driver_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.driver.license_number)

    def test_license_number_in_driver_change(self):
        url = reverse("admin:taxi_driver_change", args=[self.driver.id])
        response = self.client.get(url)

        self.assertContains(response, self.driver.license_number)

    def test_additional_info_fields_in_driver_add(self):
        url = reverse("admin:taxi_driver_add")
        response = self.client.get(url)

        self.assertContains(response, "license_number")
        self.assertContains(response, "Additional info")


class AdminSiteManufacturerTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user",
            password="1qazcde3",
        )
        self.client.force_login(self.admin_user)

    def test_manufacturer_is_register_in_admin(self):
        url = reverse("admin:taxi_manufacturer_changelist")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class AdminSiteCarTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user",
            password="1qazcde3",
        )
        self.client.force_login(self.admin_user)

    def test_car_is_register_in_admin(self):
        url = reverse("admin:taxi_car_changelist")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class GitignoreTests(TestCase):
    def test_gitignore_exist(self):
        file_exists = os.path.exists('.gitignore')
        assert file_exists

    def test_gitignore_has_correct_content(self):
        with open(".gitignore", "r") as gitignore:
            gitignore_content = gitignore.read()

            assert "idea" in gitignore_content
            assert "sqlite3" in gitignore_content
            assert "pyc" in gitignore_content
class ManufacturerModelTest(TestCase):
    def test_create_manufacturer(self):
        manufacturer = Manufacturer.objects.create(name="Toyota", country="Japan")
        self.assertEqual(manufacturer.name, "Toyota")
        self.assertEqual(manufacturer.country, "Japan")

class CarModelTest(TestCase):
    def test_create_car(self):
        manufacturer = Manufacturer.objects.create(name="Toyota", country="Japan")
        car = Car.objects.create(model="Corolla", manufacturer=manufacturer)
        self.assertEqual(car.model, "Corolla")
        self.assertEqual(car.manufacturer.name, "Toyota")

class DriverModelTest(TestCase):
    def test_create_driver(self):
        driver = Driver.objects.create_user(username="testdriver", password="password123", license_number="ABC123")
        self.assertEqual(driver.username, "testdriver")
        self.assertEqual(driver.license_number, "ABC123")