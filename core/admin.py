from django.contrib import admin
from .models import Messages, Products, Quote
# Register your models here.

class AdminMessages(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Message')

class AdminProducts(admin.ModelAdmin):
    list_display = ('Name', 'Description')

class AdminQuote(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Product', 'Quantity', 'Description')

admin.site.register(Messages, AdminMessages)
admin.site.register(Products,AdminProducts)
admin.site.register(Quote,AdminQuote)