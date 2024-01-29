from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Manufacturer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    country = models.CharField(max_length=30)

    class Meta:
        ordering = ["country"]

    def __str__(self):
        return self.name

class Driver(AbstractUser):
    license_number = models.CharField(max_length=30, unique=True)

    groups = models.ManyToManyField(Group, related_name="drivers")
    user_permissions = models.ManyToManyField(Permission, related_name="drivers")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.license_number}"

class Car(models.Model):
    model = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(Driver,
                                     through='CarDriverRelation',
                                     related_name='cars')

    def __str__(self):
        return (f"{self.manufacturer} {self.model}"
                f"({self.manufacturer.country})")


class CarDriverRelation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='driver_relations')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='car_relations')

    def __str__(self):
        return f"Relation between {self.driver} and {self.car}"