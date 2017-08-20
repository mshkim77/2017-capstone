from django.conf.urls import url
from .views import add_new_word, get_word_emotions

urlpatterns = [
    url(r'^new/', add_new_word),
    url(r'^(?P<word>\d+)', get_word_emotions),
]