from django.conf.urls import url
from .views import post_new_audio, get_audio_info, analyze_audio_file

urlpatterns = [
    url(r'^new/', post_new_audio),
    url(r'^analyze/(?P<audio_id>\d+)/$', analyze_audio_file),
    url(r'^(?P<audio_id>\d+)', get_audio_info),
]
