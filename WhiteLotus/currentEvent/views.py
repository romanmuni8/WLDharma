from django.shortcuts import render

from django.apps import apps
Event = apps.get_model('cal', 'Event')


def events(request):
    event_list = Event.objects.all()
    return render(request, 'currentEvent/events.html', {'event_list': event_list})
