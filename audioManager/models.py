from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

# Create your models here.
class AudioFile(models.Model):
    file_id = models.AutoField(primary_key=True, unique=True, editable=False)
    original_file = models.FileField(validators=[FileExtensionValidator(('wav', 'mp3', 'm4a'))],
                                     upload_to="original_audio/%Y/%m/%d/")
    upload_date = models.DateTimeField(editable=False, default=timezone.now())