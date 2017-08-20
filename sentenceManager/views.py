from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Sentence
from .apps import getSentenceFromAudio
from audioManager.models import AudioFile

def get_sentence_data(request, audio_id):
    sentenceData = get_object_or_404(Sentence, pk=AudioFile(pk=audio_id))

    return JsonResponse({
        "sentence": sentenceData.sentence,
    })

def request_sentence_data(request, audio_id):
    getSentenceFromAudio(audio_id)

    return JsonResponse({
        "job_id": "1",
    })
