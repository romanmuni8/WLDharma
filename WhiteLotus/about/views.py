from django.shortcuts import render
from .models import AboutPageText, Teacher


def about(request):
    text = None
    if AboutPageText.objects.count() != 0:
        text = AboutPageText.objects.get()
    teachers = Teacher.objects.all()
    return render(request, "about/about.html", {'aboutPageText': text, 'teachers': teachers})
