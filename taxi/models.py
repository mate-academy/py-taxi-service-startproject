from django.contrib.auth.models import AbstractUser

from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser, ):
    license_number = models.CharField(max_length=63, unique=True, )
    email = models.EmailField()
    password = models.CharField(max_length=63, )
    first_name = models.CharField(max_length=63, )
    last_name = models.CharField(max_length=63, )


def __str__(self, ):
    return f"{self.first_name} {self.last_name}"


class Car(models.Model, ):
    model = models.CharField(max_length=63, )
    manufacturer = models.OneToOneField(Manufacturer,
                                        on_delete=models.CASCADE,
                                        unique=True,
                                        )
    drivers = models.ManyToManyField(Driver, blank=True, )

    def __str__(self, ):
        return f"{self.model}"
