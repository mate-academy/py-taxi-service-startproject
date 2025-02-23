from django.db import models
from django.contrib.auth.models import AbstractUser

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

 
        """
    -->from django.contrib.auth.models import AbstractUser
    This model inherits all the fields and methods from AbstractUser,
    which already includes:
      - username
      - email
      - first_name
      - last_name
      - password
      - is_staff, is_superuser, etc.
    """
class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.username} ({self.license_number})"
    
class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    # Many-to-many relationship between Car and Driver
    drivers = models.ManyToManyField(
        Driver,
        related_name='cars',
        blank=True
    )

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"
    
class Meta:
     pass