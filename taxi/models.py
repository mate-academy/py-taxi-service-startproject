from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}, {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique = True)

    class Meta:
        ordering = ["license_number"]
    
    def __str__(self):
        return f"{self.username}; {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    driver = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="car")

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return f"{self.manufacturer.name}, {self.model}, {self.manufacturer.country}"
