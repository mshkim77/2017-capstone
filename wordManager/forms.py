from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class FormAddNewWord(forms.Form):
    word = forms.CharField()

    rage = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    loathing = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    grief = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    amazement = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    terror = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    admiration = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    ecstasy = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    vigilance = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
