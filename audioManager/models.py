from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

# Create your models here.
class AudioFile(models.Model):
    file_id = models.AutoField(primary_key=True, unique=True, editable=False)
    file = models.FileField(validators=[FileExtensionValidator(('wav', 'mp3', 'm4a'))],
                            upload_to="original_audio/%Y/%m/%d/")
    converted_file = models.FileField(null=True)
    upload_date = models.DateTimeField(editable=False, default=timezone.now())

class AudioFileInfo(models.Model):
    audio = models.OneToOneField('AudioFile', on_delete=models.CASCADE, primary_key=True)
    sample_rate = models.IntegerField()
    file_length = models.FloatField()
    
