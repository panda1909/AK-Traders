from django.contrib import admin
from .models import Messages
# Register your models here.

class AdminMessages(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Message')

admin.site.register(Messages, AdminMessages )