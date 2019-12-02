from django.conf.urls import url
from . import views

app_name = 'dailyprayer'
urlpatterns = [
    url('', views.daily_prayer, name='daily_prayer')
]