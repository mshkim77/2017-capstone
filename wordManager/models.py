from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Word(models.Model):
    # 단어
    word = models.CharField(primary_key=True, null=False, unique=True, max_length= 255)

    # 감정 관련 데이터
    rage = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    loathing = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    grief = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    amazement = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    terror = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    admiration = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    ecstasy = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    vigilance = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)

