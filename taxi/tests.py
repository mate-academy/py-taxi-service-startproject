from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from taxi.models import Manufacturer, Car

class ModelsTest(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(
            name="Test Manufacturer",
            country="Test Country"
        )
        self.driver = get_user_model().objects.create_user(
            username="testdriver",
            password="testpass123",
            license_number="TEST12345"
        )
        self.car = Car.objects.create(
            model="Test Model",
            manufacturer=self.manufacturer
        )
        self.car.drivers.add(self.driver)

    def test_manufacturer_str(self):
        self.assertEqual(str(self.manufacturer), "Test Manufacturer")

    def test_car_str(self):
        self.assertEqual(str(self.car), "Test Model")

    def test_driver_str(self):
        self.assertEqual(str(self.driver), "testdriver")

    def test_car_manufacturer_relation(self):
        self.assertEqual(self.car.manufacturer, self.manufacturer)
        self.assertEqual(self.manufacturer.cars.first(), self.car)

    def test_car_drivers_relation(self):
        self.assertEqual(self.car.drivers.count(), 1)
        self.assertEqual(self.driver.cars.first(), self.car)

    def test_driver_license_number_unique(self):
        with self.assertRaises(Exception):
            get_user_model().objects.create_user(
                username="anotherdriver",
                password="testpass123",
                license_number="TEST12345")
