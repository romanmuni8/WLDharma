from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    return render(request, 'home.html')

def about(request):

    return render(request,"about.html")

def calendar(request):

    return render(request, "cal.calendar.html")


def events(request):

    return render(request,"events.html")

def pictures (request):

    return render("pictures.html")

def membership(request):

    return render("membership.html")

def dailyprayer(request):

    return render(request,"dailyPrayer.html")
