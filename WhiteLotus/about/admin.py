from django.contrib import admin
from .models import AboutPageText, Teacher


class AboutAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(AboutPageText, AboutAdmin)
