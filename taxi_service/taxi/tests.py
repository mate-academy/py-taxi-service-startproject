from django.test import TestCase
from taxi.models import Driver, Car, Manufacturer

class TaxiTests(TestCase):
    def test_create_manufacturer_and_car_and_driver(self):
        # tworzenie producenta
        manufacturer = Manufacturer.objects.create(name="Tesla")

        # tworzenie kierowcy z wymaganym license_number
        driver = Driver.objects.create_user(
            username="john_doe",
            password="ComplexPass123",
            license_number="ABC123"
        )

        # tworzenie samochodu i przypisanie kierowcy
        car = Car.objects.create(model="Model S", manufacturer=manufacturer)
        car.drivers.add(driver)

        # asercje
        self.assertEqual(Manufacturer.objects.count(), 1)
        self.assertEqual(Driver.objects.count(), 1)
        self.assertEqual(Car.objects.count(), 1)
        self.assertIn(driver, car.drivers.all())
