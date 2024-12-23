from django.contrib import admin
from .models import *

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['title','id', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'created_time','publish_time']
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'publish_time'
    search_fields = ['title','body']
    ordering = ['status','publish_time']
    
@admin.register(Category)
class CatgoryAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    search_fields = ['name','id']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email']