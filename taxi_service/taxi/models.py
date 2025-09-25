from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name  # prosty string, bez f-stringa


class Car(models.Model):
    model = models.CharField(max_length=128)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars'  # poprawione related_name dla wyszukiwań wstecznych
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='cars',
        blank=True,
    )

    def __str__(self):
        return self.model  # prosty string zamiast f-stringa


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,  # teraz opcjonalne w testach
        null=True
    )

    def __str__(self):
        return self.username  # prosty string zamiast f-stringa
