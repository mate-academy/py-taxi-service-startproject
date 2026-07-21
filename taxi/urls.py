from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="taxi/login.html"),
        name="login",
    ),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("cars/", views.cars, name="cars"),
    path("drivers/", views.drivers, name="drivers"),
    path("manufacturers/", views.manufacturers, name="manufacturers"),
]
