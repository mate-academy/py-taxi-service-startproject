from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Car, Manufacturer


class ManufacturerModelTEst(TestCase):
    def test_create_manaufacturer(self):
        manufacturer = Manufacturer.objects.create(name="Tesla", country="USA")
        self.assertEqual(manufacturer.name, "Tesla")
        self.assertEqual(manufacturer.country, "USA")


class CarModelTest(TestCase):
    def test_create_car(self):
        manufacturer = Manufacturer.objects.create(name="Tesla", country="USA")
        car = Car.objects.create(model="x", manufacturer=manufacturer)
        self.assertEqual(car.model, "x")
        self.assertEqual(car.manufacturer.name, "Tesla")


class DriverModelTest(TestCase):
    def test_create_driver(self):
        User = get_user_model()
        driver = User.objects.create_user(username="driver1", password="password", license_number="12345qwerty")
        self.assertEqual(driver.username, "driver1")
        self.assertEqual(driver.password, "password")
        self.assertEqual(driver.license_number, "12345qwerty")