from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def pictures(request):
    return render("pictures.html")


def membership(request):
    return render("membership.html")

