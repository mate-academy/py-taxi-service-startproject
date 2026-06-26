from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class DriverUserManager(BaseUserManager):
    def create_user(
            self, username,
            license_number, password=None, **extra_fields
    ):
        if not username:
            raise ValueError("The Username field must be set")
        if not license_number:
            raise ValueError("The License Number field must be set")
        user = self.model(
            username=username, license_number=license_number, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, username,
            license_number=None,
            password=None, **extra_fields
    ):
        if license_number is None:
            license_number = "ADMIN123"
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(
            username, license_number, password, **extra_fields
        )


class Driver(AbstractUser):
    license_number = models.CharField(unique=True, max_length=100)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="driver_groups",
        blank=True,
        help_text="The"
                  " groups this driver belongs to. A"
                  " driver will get all permissions"
                  " granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="driver_permissions",
        blank=True,
        help_text="Specific permissions for this driver.",
    )
    objects = DriverUserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["license_number"]

    def __str__(self):
        return self.username

class Manufacturer(models.Model):
    name = models.CharField(unique=True, max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(unique=True, max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField("Driver", related_name="cars")

    def __str__(self):
        return self.model
