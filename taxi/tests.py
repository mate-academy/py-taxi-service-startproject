from django.test import TestCase
from django.db import IntegrityError

from taxi.models import Driver, Manufacturer


class DjangoTaxiTestCase(TestCase):
    def setUp(self):
        Manufacturer.objects.create(name="ZAZ",
                                    country="Ukraine")

        Driver.objects.create(username="Andry",
                              email="andry@some.com",
                              password="1qwerty6",
                              license_number= "1234567890")

    def test_manufacturers_name_should_be_unique(self):
        with self.assertRaises(IntegrityError):
            Manufacturer.objects.create(name="ZAZ",
                                        country="Ukraine")

    def test_drivers_license_should_be_unique(self):
        with self.assertRaises(IntegrityError):
            Driver.objects.create(username="Andry",
                                  email="andry@some.com",
                                  password="1qwerty6",
                                  license_number="1234567890")

