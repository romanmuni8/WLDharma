from django.shortcuts import render
from .models import AboutPageText


def about(request):
    text = AboutPageText.objects.get()
    return render(request, "about/about.html", {'aboutPageText': text})
