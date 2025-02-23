from django.contrib import admin
#After creating the models, you can register them with the Django admin site.
#To do this, you need to import the models and then register them using admin.site.register().
#For example, to register the Manufacturer, Driver, and Car models, you can add the following code to the taxi/admin.py file:
from .models import Manufacturer, Driver, Car
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Driver)
admin.site.register(Car)


class DriverAdmin(UserAdmin):
    """
    Custom admin to ensure license_number displays like other user fields.
    """

    # 1) Add `license_number` to the default fieldsets, so you see it in the edit form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('license_number',)}),
    )

    # 2) Display `license_number` in the main user list
    list_display = UserAdmin.list_display + ('license_number',)

    # 3) (Optional) Include `license_number` when creating new users in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('license_number',),
        }),
    )


    """
    Custom admin class for Driver, which inherits from AbstractUser.
    We add license_number under a new 'Additional info' heading in the edit form.
    """

    # Extend the default fieldsets to include 'license_number' in a new section
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {
            'fields': ('license_number',),
        }),
    )

    # (Optional) If you want to add 'license_number' at user creation too:
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {
            'classes': ('wide',),
            'fields': ('license_number',),
        }),
    )

    # Optionally, display license_number in the user list
    list_display = UserAdmin.list_display + ('license_number',)

class CarAdmin(admin.ModelAdmin):
    # This tells Django Admin to allow searching on the 'model' field
    search_fields = ('model',)

    # (Optional) Control which columns appear in the admin list
    list_display = ('model', 'manufacturer')

    # This adds a filter sidebar for the 'manufacturer' field
    list_filter = ('manufacturer',)  