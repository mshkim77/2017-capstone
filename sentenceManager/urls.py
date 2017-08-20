from django.conf.urls import url
from .views import request_sentence_data, get_sentence_data

urlpatterns = [
    url(r'^(?P<audio_id>\d+)', request_sentence_data),
]