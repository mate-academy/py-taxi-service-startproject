from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse:
    context = {
        "some_var": "some variable",
    }
    return render(request, "taxi/index.html", context)