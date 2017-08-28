from django.conf.urls import url
from .views import record_new_audio, post_new_audio, post_new_audio_with_emotions, get_audio_info, analyze_audio_file, post_new_audio_with_emotions_and_features

urlpatterns = [
    url(r'^record/', record_new_audio),
    url(r'^add/', post_new_audio),
    url(r'^emotion-add/', post_new_audio_with_emotions),
    url(r'^feature-add/', post_new_audio_with_emotions_and_features),
    # url(r'^analyze/(?P<audio_id>\d+)/$', analyze_audio_file),
    url(r'^(?P<audio_id>\d+)', get_audio_info),
]
