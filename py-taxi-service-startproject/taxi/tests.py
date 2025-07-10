from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Manufacturer, Car, Driver


class ManufacturerModelTest(TestCase):
    def test_str_representation(self):
        manufacturer = Manufacturer.objects.create(name="Toyota", country="Japan")
        self.assertEqual(str(manufacturer), "Toyota (Japan)")


class CarModelTest(TestCase):
    def test_str_representation(self):
        manufacturer = Manufacturer.objects.create(name="Ford", country="USA")
        car = Car.objects.create(model="Mustang", manufacturer=manufacturer)
        self.assertEqual(str(car), "Mustang")


class DriverModelTest(TestCase):
    def test_str_representation(self):
        driver = get_user_model().objects.create_user(
            username="driver1", password="test1234", license_number="AB12345"
        )
        self.assertEqual(str(driver), "driver1 (AB12345)")
