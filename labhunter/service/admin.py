from django.contrib import admin

# Register your models here.
# lab_hunter_biletskyi

from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'topic', 'work_number')
    list_display_links = ('id', 'topic')
    search_fields = ('teacher', 'topic')
    prepopulated_fields = {'file_slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name')
    list_display_links = ('id', 'cat_name')
    search_fields = ('cat_name',)
    prepopulated_fields = {'cat_slug': ('cat_name',)}


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_name', 'course', 'semester')
    list_display_links = ('id', 'sub_name')
    search_fields = ('sub_name', 'course', 'semester')
    prepopulated_fields = {'sub_slug': ('sub_name',)}


class OrderItemAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Files, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subject, SubjectAdmin)
#admin.site.register(OrderItem, OrderItemAdmin)
#admin.site.register(Order, OrderAdmin)
