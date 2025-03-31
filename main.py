import random

import init_django_orm # noqa: F401
import json
from django.db import transaction
from django.contrib.auth import get_user_model

from taxi.models import Manufacturer, Car, Driver


def main():
    with open("cars.json", "r") as json_file:
        cars_dict = json.load(json_file)

    with open("drivers.json", "r") as json_file:
        drivers_dict = json.load(json_file)

    with transaction.atomic():
        for driver_dict in drivers_dict:
            user = get_user_model().objects.get_or_create(
                username=driver_dict["username"],
                first_name=driver_dict["first_name"],
                last_name=driver_dict["last_name"],
                license_number=driver_dict["license_number"],
            )
            if user[1]:
                user[0].set_password("1234")


    with transaction.atomic():
        for car_dict in cars_dict:
            manufacturer = Manufacturer.objects.get_or_create(
                name=car_dict["manufacturer"],
                country=car_dict["country"]
            )[0]
            car = Car.objects.get_or_create(
                model=car_dict["model"],
                manufacturer=manufacturer,
            )[0]
            car.drivers.clear()
            for _ in range(random.randint(1, 3)):
                drivers = list(Driver.objects.exclude(id=1))
                driver = random.choice(drivers)
                car.drivers.add(driver)
            car.save()


if __name__ == '__main__':
    main()
