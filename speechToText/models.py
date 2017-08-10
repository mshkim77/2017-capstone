from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from audioManager.models import AudioFile

# Create your models here.
# class Sentence(models.Model):
#     audio_id = models.ForeignKey('AudioFile', on_delete=models.CASCADE, primary_key=True)
#     sentence = models.TextField()
#     reliability = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0), ])
#     hasError = models.NullBooleanField(null=True)
#     words = models.ManyToManyField('Word')
#
# class Word(models.Model):
#     word = models.CharField(primary_key=True, null=False, unique=True, max_length= 255)
#     type = models.CharField(max_length=5, null=True)