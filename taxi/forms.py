from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Driver

class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = ("username", "first_name", "last_name", "email", "license_number")

class DriverChangeForm(UserChangeForm):
    class Meta:
        model = Driver
        fields = ("username", "first_name", "last_name", "email", "license_number")
