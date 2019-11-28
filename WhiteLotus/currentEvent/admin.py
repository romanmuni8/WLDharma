from django.contrib import admin
from .models import News, Images


class ImagesAdmin(admin.TabularInline):
    model = Images


class NewsAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin, ]


admin.site.register(News, NewsAdmin)
