from django.contrib.auth.models import AbstractUser
from django.db import models
import taxi_service.settings as settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} from {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Driver(AbstractUser):
    licence_number = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
