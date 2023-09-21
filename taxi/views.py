from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def show_off(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "<html>"
        "<h1>"
        "Hey, I've goddamn it done it!"
        "</h1>"
        "</html"
    )

