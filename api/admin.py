from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

from .models import Task, Admin_Messages

class TaskAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'title', 'bully_rate', 'platform', 'time_now') 
    list_filter = ('time_now','platform',)
    search_fields = ('title', 'from_user', 'to_user')

class AdminMessage(admin.ModelAdmin):
    list_display = ('name','email', 'message') 
    search_fields = ('name', 'email')


admin.site.register(Task, TaskAdmin)
admin.site.unregister(Group)

admin.site.register(Admin_Messages, AdminMessage)