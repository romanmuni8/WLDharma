from django.shortcuts import render
from .models import News, Images
from django.apps import apps
Event = apps.get_model('cal', 'Event')


def events(request):
    event_list = Event.objects.all()
    news_list = News.objects.all()
    images = Images.objects.all()
    return render(request, 'currentEvent/events.html', {'event_list': event_list, 'news_list': news_list, 'news_images': images})
