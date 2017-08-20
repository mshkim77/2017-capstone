from django.contrib import admin
from .models import AudioFile, AudioFeature

class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'file', 'upload_date')

class AudioFeatureAdmin(admin.ModelAdmin):
    list_display = ('audio', 'tempo')

admin.site.register(AudioFile, AudioFileAdmin)
admin.site.register(AudioFeature, AudioFeatureAdmin)