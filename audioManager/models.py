from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
import base64

# Create your models here.
class AudioFile(models.Model):
    file_id = models.AutoField(primary_key=True, unique=True, editable=False)
    file = models.FileField(validators=[FileExtensionValidator(('wav', 'mp3', 'm4a'))],
                            upload_to="original_audio/%Y/%m/%d/")
    upload_date = models.DateTimeField(editable=False, default=timezone.now())

class AudioFeature(models.Model):
    audio = models.OneToOneField(AudioFile, on_delete=models.CASCADE, primary_key=True)

    mfcc = models.BinaryField()

    freq_magnitude = models.BinaryField()
    freq_phase = models.BinaryField()
    pitch = models.BinaryField()
    tempo = models.FloatField()


