from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Manufacturer, Car


class ManufacturerModelTest(TestCase):
    def test_str_method(self):
        manufacturer = Manufacturer.objects.create(name="Toyota", country="Japan")
        self.assertEqual(str(manufacturer), "Toyota Japan")


class CarModelTest(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(name="BMW", country="Germany")

    def test_str_method(self):
        car = Car.objects.create(model="X5", manufacturer=self.manufacturer)
        self.assertEqual(str(car), "BMW X5")


class DriverModelTest(TestCase):
    def test_str_method(self):
        driver = get_user_model().objects.create_user(
            username="driver1",
            password="testpass123",
            license_number="ABC12345",
            first_name="John",
            last_name="Doe"
        )
        self.assertEqual(str(driver), "John Doe (ABC12345)")

