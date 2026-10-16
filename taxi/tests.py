from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Manufacturer


class TaxiModelTests(TestCase):
    def test_unique_manufacturer_name(self):
        Manufacturer.objects.create(name="Toyota", country="Japan")
        with self.assertRaises(IntegrityError), transaction.atomic():
            Manufacturer.objects.create(name="Toyota", country="Japan")

    def test_unique_driver_license(self):
        get_user_model().objects.create_user(
            username="first", license_number="ABC12345"
        )
        with self.assertRaises(IntegrityError), transaction.atomic():
            get_user_model().objects.create_user(
                username="second", license_number="ABC12345"
            )

    def test_car_can_have_multiple_drivers_and_reverse_relations(self):
        manufacturer = Manufacturer.objects.create(
            name="Toyota", country="Japan"
        )
        car = Car.objects.create(model="Prius", manufacturer=manufacturer)
        drivers = [
            get_user_model().objects.create_user(
                username=f"driver{number}", license_number=f"ABC1234{number}"
            )
            for number in range(2)
        ]
        car.drivers.add(*drivers)
        self.assertEqual(car.drivers.count(), 2)
        self.assertEqual(list(drivers[0].cars.all()), [car])
        self.assertEqual(list(manufacturer.cars.all()), [car])


class CarAdminTests(TestCase):
    def setUp(self):
        admin = get_user_model().objects.create_superuser(
            username="admin", password="test-password",
            license_number="ADM12345",
        )
        self.client.force_login(admin)
        self.toyota = Manufacturer.objects.create(
            name="Toyota", country="Japan"
        )
        ford = Manufacturer.objects.create(name="Ford", country="USA")
        self.prius = Car.objects.create(
            model="Prius", manufacturer=self.toyota
        )
        Car.objects.create(model="Focus", manufacturer=ford)

    def test_search_by_model(self):
        response = self.client.get(
            reverse("admin:taxi_car_changelist"), {"q": "Pri"}
        )
        self.assertEqual(
            list(response.context["cl"].queryset), [self.prius]
        )

    def test_filter_by_manufacturer(self):
        response = self.client.get(
            reverse("admin:taxi_car_changelist"),
            {"manufacturer__id__exact": self.toyota.pk},
        )
        self.assertEqual(
            list(response.context["cl"].queryset), [self.prius]
        )

    def test_admin_creates_driver_with_license_and_hashed_password(self):
        response = self.client.post(
            reverse("admin:taxi_driver_add"),
            {
                "username": "new-driver",
                "password1": "Strong-test-password-729!",
                "password2": "Strong-test-password-729!",
                "license_number": "NEW12345",
                "usable_password": "true",
            },
        )
        self.assertEqual(response.status_code, 302)
        driver = get_user_model().objects.get(username="new-driver")
        self.assertEqual(driver.license_number, "NEW12345")
        self.assertTrue(driver.check_password("Strong-test-password-729!"))
