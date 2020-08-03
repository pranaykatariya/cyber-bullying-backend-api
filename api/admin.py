from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Task, Admin_Messages, AadharCard,Report, Image, Video, Web

# Register your models here.

admin.site.unregister(Group)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'title', 'bully_rate', 'platform', 'time_now') 
    list_filter = ('time_now','platform',)
    search_fields = ('title', 'from_user', 'to_user')

class AdminMessage(admin.ModelAdmin):
    list_display = ('name','email', 'message') 
    search_fields = ('name', 'email')

class AadharAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'aadharno', 'email', 'dob', 'mobile') 
    # list_filter = ('time_now','platform',)
    search_fields = ('firstname', 'lastname', 'aadharno', 'email', 'mobile')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('complain_id', 'complainer', 'victim', 'abuser', 'tweet', 'time_now') 
    list_filter = ('time_now',)
    search_fields = ('complain_id', 'complainer', 'victim', 'abuser',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('complain_id', 'platform_id', 'url', 'platform', 'result', 'time_now') 
    list_filter = ('time_now','platform',)
    search_fields = ('complain_id', 'platform', 'url',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('complain_id', 'platform_id', 'url', 'platform', 'result', 'time_now') 
    list_filter = ('time_now','platform',)
    search_fields = ('complain_id', 'platform', 'url',)


class WebAdmin(admin.ModelAdmin):
    list_display = ('complain_id', 'url', 'result','time_now',) 
    list_filter = ('time_now',)
    search_fields = ('complain_id', 'url',)



admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
# admin.site.register(Web, WebAdmin)

admin.site.register(Task, TaskAdmin)
admin.site.register(Admin_Messages, AdminMessage)
# admin.site.register(AadharCard, AadharAdmin)
admin.site.register(Report,ReportAdmin)