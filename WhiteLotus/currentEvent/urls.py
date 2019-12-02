from django.conf.urls import url
from . import views

app_name = 'currentEvent'
urlpatterns = [
    url('', views.events, name='events')
]
