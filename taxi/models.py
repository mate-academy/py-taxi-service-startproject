from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models



class Manufactured(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_name"
            )
        ]


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufactured = models.ForeignKey("Manufactured", on_delete=models.CASCADE)
    drivers = models.ManyToManyField("Driver", related_name="cars")


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["license_number"],
                name="unique_license_number"
            )
        ]

