from django.db import models
from django.utils import timezone

from audioManager.models import AudioFile

# Create your models here.
class Job(models.Model):
    audio = models.ForeignKey(AudioFile, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=128)
    last_update = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        super(Job, self).save(*args, **kwargs)
