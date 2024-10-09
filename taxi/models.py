from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

# Create your models here.
class Manufacturer(models.Model):
  name = models.CharField(max_length=255, unique=True, blank=False, null=False)
  country = models.CharField(max_length=255)

  class Meta:
    ordering = ("name",)

  def __str__(self):
    return f"{self.name} : {self.country}"
  

class Driver(AbstractUser):
  license_number = models.CharField(max_length=255, unique=True, blank=False, null=False)

  class Meta:
    ordering = ("license_number",)

  def __str__(self):
    return self.username


class Car(models.Model):
  model = models.CharField(max_length=255)
  manufacturer = models.ForeignKey(
    Manufacturer,
    on_delete=models.CASCADE,
    related_name="cars",
  )
  drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

  class Meta:
    ordering = ("model",)

  def __str__(self):
      return self.model
