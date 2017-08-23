from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('audio', 'status', 'last_update')

admin.site.register(Job, JobAdmin)