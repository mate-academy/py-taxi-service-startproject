from django.urls import path

from taxi.views import index


app_name = "taxi"

urlpatterns = [
    path("", index, name="index"),
]
