from django.conf.urls import url
from .views import get_sentence_data

urlpatterns = [
    url(r'^(?P<audio_id>\d+)', get_sentence_data),
]