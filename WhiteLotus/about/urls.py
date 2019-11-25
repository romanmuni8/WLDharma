from django.conf.urls import url
from . import views

# adding this so when i merge this doesnt get auto deleted

app_name = 'about'
urlpatterns = [
    url('', views.about, name='about'),
]