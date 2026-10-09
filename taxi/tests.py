from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Manufacturer


class ManufacturerModelTests(TestCase):
    def test_str_returns_name(self):
        manufacturer = Manufacturer.objects.create(name="Toyota", country="Japan")

        self.assertEqual(str(manufacturer), "Toyota")

    def test_name_is_unique(self):
        Manufacturer.objects.create(name="Toyota", country="Japan")

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Manufacturer.objects.create(name="Toyota", country="USA")


class DriverModelTests(TestCase):
    def test_license_number_is_stored(self):
        driver = get_user_model().objects.create_user(
            username="driver1",
            password="pass12345",
            license_number="DRV12345",
        )

        self.assertEqual(driver.license_number, "DRV12345")
        self.assertEqual(str(driver), "driver1")

    def test_license_number_is_unique(self):
        get_user_model().objects.create_user(
            username="driver1",
            password="pass12345",
            license_number="DRV12345",
        )

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                get_user_model().objects.create_user(
                    username="driver2",
                    password="pass12345",
                    license_number="DRV12345",
                )


class CarModelTests(TestCase):
    def test_car_links_manufacturer_and_drivers(self):
        manufacturer = Manufacturer.objects.create(name="Toyota", country="Japan")
        driver = get_user_model().objects.create_user(
            username="driver1",
            password="pass12345",
            license_number="DRV12345",
        )
        car = Car.objects.create(model="Camry", manufacturer=manufacturer)
        car.drivers.add(driver)

        self.assertEqual(str(car), "Camry")
        self.assertEqual(manufacturer.cars.get(), car)
        self.assertEqual(car.drivers.get(), driver)
        self.assertEqual(driver.cars.get(), car)


class AdminSiteTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user",
            password="1qazcde3",
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username="test.user",
            password="2wsxvfr4",
            license_number="TES12345",
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

    def test_manufacturer_and_car_are_registered(self):
        manufacturer_response = self.client.get(
            reverse("admin:taxi_manufacturer_changelist")
        )
        car_response = self.client.get(reverse("admin:taxi_car_changelist"))

        self.assertEqual(manufacturer_response.status_code, 200)
        self.assertEqual(car_response.status_code, 200)
