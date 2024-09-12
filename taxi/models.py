from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=69)

    def __str__(self):
        return f"{self.name}; country: {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=69,
                                      unique=True)
    username = models.CharField(max_length=69,
                                unique=True
                                )
    email = models.EmailField(max_length=69)
    password = models.CharField(max_length=69)
    first_name = models.CharField(max_length=69)
    last_name = models.CharField(max_length=69)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"Driver username:{self.username}; " \
               f"password: {self.password}; " \
               f"license_number: {self.license_number}; " \
               f"data: {self.first_name} {self.last_name} {self.email}"


class Car(models.Model):
    model = models.CharField(max_length=69)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"Car model: {self.model} " \
               f"manufacturer: {self.manufacturer} " \
               f"drivers: {self.drivers}"
