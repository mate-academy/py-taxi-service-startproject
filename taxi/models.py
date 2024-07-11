from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20)
    username = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    groups = models.ManyToManyField(Group, related_name='driver_set')
    user_permissions = models.ManyToManyField(Permission, related_name='driver_set')

    def __str__(self):
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name='cars')

    def __str__(self):
        return self.model
