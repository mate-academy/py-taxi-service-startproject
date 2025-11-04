# taxi/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Manufacturer, Car

Driver = get_user_model()


class ModelsTestCase(TestCase):
    def test_create_manufacturer_and_car_and_driver(self):
        m = Manufacturer.objects.create(name="Toyota", country="Japan")
        car = Car.objects.create(model="Corolla", manufacturer=m)
        driver = Driver.objects.create_user(username="john", password="pass1234", license_number="ABC123")
        car.drivers.add(driver)

        self.assertEqual(Manufacturer.objects.count(), 1)
        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(Driver.objects.filter(username="john").count(), 1)
        self.assertIn(driver, car.drivers.all())
