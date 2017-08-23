from django.db import models
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
class AudioFile(models.Model):
    file_id = models.AutoField(primary_key=True, unique=True, editable=False)
    file = models.FileField(validators=[FileExtensionValidator(('wav', 'mp3', 'm4a', 'webm', 'ogg'))],
                            upload_to="original_audio/%Y/%m/%d/")
    converted_file = models.FileField(validators=[FileExtensionValidator(('wav',))],
                                      upload_to="original_audio/%Y/%m/%d/", null=True)
    upload_date = models.DateTimeField(editable=False, default=timezone.now())

class AudioFeature(models.Model):
    audio = models.OneToOneField(AudioFile, on_delete=models.CASCADE, primary_key=True)
    duration = models.FloatField(default=0.0)
    tempo = models.FloatField(default=0.0)

    # 특성 추출 데이터
    avg_mfcc = models.FloatField(default=0.0)
    max_mfcc = models.FloatField(default=0.0)
    min_mfcc = models.FloatField(default=0.0)
    var_mfcc = models.FloatField(default=0.0)
    std_mfcc = models.FloatField(default=0.0)

    avg_ZCR = models.FloatField(default=0.0)
    var_ZCR = models.FloatField(default=0.0)
    std_ZCR = models.FloatField(default=0.0)

    avg_energy = models.FloatField(default=0.0)
    max_energy = models.FloatField(default=0.0)
    min_energy = models.FloatField(default=0.0)
    std_energy = models.FloatField(default=0.0)

    avg_harmonic = models.FloatField(default=0.0)
    avg_harmonic_in_max = models.FloatField(default=0.0)
    avg_harmonic_in_min = models.FloatField(default=0.0)

    diff_avg_harmonic_max = models.FloatField(default=0.0)
    diff_avg_harmonic_min = models.FloatField(default=0.0)
    diff_avg_harmonic_maxmin = models.FloatField(default=0.0)

    # 감정 관련 데이터
    rage = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    loathing = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    grief = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    amazement = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    terror = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    admiration = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    ecstasy = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)
    vigilance = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True)

