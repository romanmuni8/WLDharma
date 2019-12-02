from random import randrange

from django.db.models import Max
from django.shortcuts import render
from .models import DailyPractice, Practice, DailyPracticeManager
from datetime import date


def daily_prayer(request):
    dp = None
    if DailyPractice.objects.count() != 0:
        dp = DailyPractice.objects.get()
        if dp.choose_date != date.today():
            dp.chosen = get_random_practice()
            dp.choose_date = date.today()
            dp.save()
    else:
        dp = DailyPractice.objects.create_daily_practice(chosen=get_random_practice(), choose_date=date.today())
    return render(request, 'dailyprayer/dailyprayer.html')


def get_random_practice():
    max_id = Practice.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = randrange(1, max_id)
        practice = Practice.objects.filter(pk=pk).first()
        if practice:
            return practice
