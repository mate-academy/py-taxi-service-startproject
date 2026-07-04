from django.contrib.auth.models import AbstractUser


from django.db import models



class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name} ({self.country})"



class Driver(AbstractUser):
    license_number = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Car(models.Model):
    model = models.CharField(max_length=63, )
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    driver = models.ManyToManyField(Driver)

    def __str__(self):
        return f"{self.model} ({self.manufacturer}) {self.driver}"
