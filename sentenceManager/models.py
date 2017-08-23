from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from audioManager.models import AudioFile
from wordManager.models import Word

# Create your models here.
class Sentence(models.Model):
    audioFile = models.OneToOneField(AudioFile, on_delete=models.CASCADE, primary_key=True)
    sentence = models.TextField()
    reliability = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0), ])
    hasError = models.NullBooleanField(null=True)
    words = models.ManyToManyField(Word)