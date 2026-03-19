from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

class Driver(AbstractUser):
    license_number = models.CharField(unique=True, max_length = 20)
    groups = models.ManyToManyField(
        Group,
        related_name='driver_set',
        blank=True,
        help_text='The groups this driver belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='driver_permissions_set',
        blank=True,
        help_text='Specific permissions for this driver.',
        verbose_name='user permissions',
    )
    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

settings.AUTH_USER_MODEL = 'taxi.Driver'

class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name="cars")
