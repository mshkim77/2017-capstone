from django.conf.urls import url
from .views import get_job_status

urlpatterns = [
    url(r'^status/(?P<job_id>\d+)/$', get_job_status),
]
