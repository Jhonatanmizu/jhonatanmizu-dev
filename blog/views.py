from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request:HttpRequest) -> HttpResponse:
    return render(request, "blog/pages/index.html")
