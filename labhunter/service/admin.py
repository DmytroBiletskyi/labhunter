from django.contrib import admin

# Register your models here.

from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'topic', 'work_number')
    list_display_links = ('id', 'topic')
    search_fields = ('teacher', 'topic')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name')
    list_display_links = ('id', 'cat_name')
    search_fields = ('name',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_name', 'course', 'semester')
    list_display_links = ('id', 'sub_name')
    search_fields = ('sub_name', 'course', 'semester')


admin.site.register(Files, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subject, SubjectAdmin)
