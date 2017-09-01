from django.contrib import admin
from .models import AudioFile, AudioFeature, SampleAudioFeatures

class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'file', 'upload_date')

class AudioFeatureAdmin(admin.ModelAdmin):
    list_display = ('audio', 'duration', 'tempo',
               'avg_mfcc', 'max_mfcc', 'min_mfcc', 'var_mfcc', 'std_mfcc',
               'avg_ZCR', 'var_ZCR', 'std_ZCR',
               'avg_energy', 'max_energy', 'min_energy', 'std_energy',
               'avg_harmonic', 'avg_harmonic_in_max', 'avg_harmonic_in_min',
               'diff_avg_harmonic_max', 'diff_avg_harmonic_min', 'diff_avg_harmonic_maxmin')

class SampleAudioFeaturesAdmin(admin.ModelAdmin):
    list_display = ('data_id', 'audio', 'duration', 'tempo',
               'avg_mfcc', 'max_mfcc', 'min_mfcc', 'var_mfcc', 'std_mfcc',
               'avg_ZCR', 'var_ZCR', 'std_ZCR',
               'avg_energy', 'max_energy', 'min_energy', 'std_energy',
               'avg_harmonic', 'avg_harmonic_in_max', 'avg_harmonic_in_min',
               'diff_avg_harmonic_max', 'diff_avg_harmonic_min', 'diff_avg_harmonic_maxmin')

admin.site.register(AudioFile, AudioFileAdmin)
admin.site.register(AudioFeature, AudioFeatureAdmin)
admin.site.register(SampleAudioFeatures, SampleAudioFeaturesAdmin)