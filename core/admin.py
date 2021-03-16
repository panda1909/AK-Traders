from django.contrib import admin
from .models import Messages, Products
# Register your models here.

class AdminMessages(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Message')

class AdminProducts(admin.ModelAdmin):
    list_display = ('Name', 'Description')

admin.site.register(Messages, AdminMessages)
admin.site.register(Products,AdminProducts)
