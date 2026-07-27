from django.test import TestCase

from taxi.models import Car, Driver, Manufacturer


class TaxiModelsTests(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(
            name="Toyota",
            country="Japan",
        )

        self.driver = Driver.objects.create_user(
            username="driver1",
            password="testpassword123",
            license_number="ABC12345",
        )

        self.car = Car.objects.create(
            model="Camry",
            manufacturer=self.manufacturer,
        )

        self.car.drivers.add(self.driver)

    def test_manufacturer_created(self):
        self.assertEqual(self.manufacturer.name, "Toyota")
        self.assertEqual(self.manufacturer.country, "Japan")

    def test_driver_created(self):
        self.assertEqual(self.driver.license_number, "ABC12345")
        self.assertTrue(self.driver.check_password("testpassword123"))

    def test_car_has_manufacturer(self):
        self.assertEqual(self.car.manufacturer, self.manufacturer)

    def test_car_has_driver(self):
        self.assertIn(self.driver, self.car.drivers.all())

    def test_driver_can_access_cars(self):
        self.assertIn(self.car, self.driver.cars.all())
