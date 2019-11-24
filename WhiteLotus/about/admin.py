from django.contrib import admin
from .models import AboutPageText


class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.register(AboutPageText, AboutAdmin)
