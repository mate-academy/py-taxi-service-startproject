from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.username} - {self.license_number}"

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    groups = models.ManyToManyField(
        Group,
        related_name="driver_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="driver_user_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
