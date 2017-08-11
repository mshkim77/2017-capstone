from django import forms
from django.core.validators import FileExtensionValidator

class FormAddNewAudioFile(forms.Form):
    audio_file = forms.FileField(validators=[FileExtensionValidator(('wav', 'mp3', 'm4a'))])
