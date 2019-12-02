from django.shortcuts import render


def daily_prayer(request):
    return render(request, 'dailyprayer/dailyprayer.html')
