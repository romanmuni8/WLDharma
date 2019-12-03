from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from datetime import date, timedelta

Event = apps.get_model('cal', 'Event')
DailyPrayer = apps.get_model('dailyprayer', 'DailyPractice')
About = apps.get_model('about', 'AboutPageText')


def home(request):
    upcoming = Event.objects.raw("SELECT * FROM cal_event WHERE start_time BETWEEN \'" + str(date.today()) + "\' AND \'" + str(date.today() + timedelta(30)) + "\'")
    return render(request, 'home.html', {'about': About.objects.get().text,
                                         'event_list': upcoming,
                                         'daily': DailyPrayer.objects.get()})


def pictures(request):
    return render("pictures.html")


def membership(request):
    return render("membership.html")

