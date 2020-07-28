from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'title', 'bully_rate', 'platform', 'time_now') 
    list_filter = ('time_now','platform',)
    search_fields = ('title', 'from_user', 'to_user')


admin.site.register(Task, TaskAdmin)
admin.site.unregister(Group)