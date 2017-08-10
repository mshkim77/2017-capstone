from django.contrib import admin
from .models import AudioFile

class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'original_file', 'upload_date')


admin.site.register(AudioFile, AudioFileAdmin)