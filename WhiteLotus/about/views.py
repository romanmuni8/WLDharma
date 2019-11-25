from django.shortcuts import render
from .models import AboutPageText, Teacher


def about(request):
    text = AboutPageText.objects.get()
    teachers = Teacher.objects.all()
    return render(request, "about/about.html", {'aboutPageText': text, 'teachers': teachers})
