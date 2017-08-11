from django.conf.urls import url
from .views import post_new_audio, get_audio_info

urlpatterns = [
    url(r'^upload/', post_new_audio),
    url(r'^(?P<audio_id>\d+)', get_audio_info),
]
