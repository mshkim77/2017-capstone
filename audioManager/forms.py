from django import forms
from django.core.validators import FileExtensionValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from material import Layout, Row

class FormAddNewAudioFile(forms.Form):
    audio_file = forms.FileField(validators=[FileExtensionValidator(('wav', 'mp3', 'm4a', 'webm', 'ogg'))])

class FormAddNewAudioFileWithEmotion(forms.Form):
    audio_file = forms.FileField(validators=[FileExtensionValidator(('wav', 'mp3', 'm4a', 'webm', 'ogg'))])

    rage = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="분노")
    loathing = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="혐오")
    grief = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="슬픔")
    amazement = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="놀람")
    terror = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="공포")
    admiration = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="감탄")
    ecstasy = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="기쁨")
    vigilance = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="경계")

    layout = Layout('audio_file',
                    Row('ecstasy', 'rage', 'grief'),
                    Row('amazement', 'terror', 'admiration'),
                    Row('loathing', 'vigilance'),
                    )

class FormAddNewAudioFileWithEmotionAndFeatures(forms.Form):
    audio_file = forms.FileField(validators=[FileExtensionValidator(('wav', 'mp3', 'm4a', 'webm', 'ogg'))], required=False)

    rage = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="분노")
    loathing = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="혐오")
    grief = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="슬픔")
    amazement = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="놀람")
    terror = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="공포")
    admiration = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="감탄")
    ecstasy = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="기쁨")
    vigilance = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], label="경계")

    # 특성 추출 데이터
    duration = forms.FloatField()
    tempo = forms.FloatField()

    avg_mfcc = forms.FloatField()
    max_mfcc = forms.FloatField()
    min_mfcc = forms.FloatField()
    var_mfcc = forms.FloatField()
    std_mfcc = forms.FloatField()

    avg_ZCR = forms.FloatField()
    var_ZCR = forms.FloatField()
    std_ZCR = forms.FloatField()

    avg_energy = forms.FloatField()
    max_energy = forms.FloatField()
    min_energy = forms.FloatField()
    std_energy = forms.FloatField()

    avg_harmonic = forms.FloatField()
    avg_harmonic_in_max = forms.FloatField()
    avg_harmonic_in_min = forms.FloatField()

    diff_avg_harmonic_max = forms.FloatField()
    diff_avg_harmonic_min = forms.FloatField()
    diff_avg_harmonic_maxmin = forms.FloatField()




