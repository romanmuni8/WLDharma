from django.contrib import admin

from .models import Event

# adding this so when i merge this doesnt get auto deleted

admin.site.register(Event)