from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, render
from .forms import FormAddNewAudioFile
from .models import AudioFile, AudioFeature
from .apps import processAudioFile

from sentenceManager.models import Sentence
from sentenceManager.apps import getSentenceFromAudio
from wordManager.apps import getWordsFromSentence

def post_new_audio(request):
    if request.method == "POST":

        form = FormAddNewAudioFile(request.POST or None, request.FILES or None)

        if form.is_valid():
            audioFile = AudioFile()
            audioFile.file = form.cleaned_data['audio_file']
            audioFile.save()

            isSaved = True
            fileID = audioFile.file_id

            return JsonResponse({"saved": isSaved, "file_id": fileID})

        else:
            return render(request, 'audio_upload_new.html', {"form": form})
            # raise Http404

    else:
        form = FormAddNewAudioFile()
        return render(request, 'audio_upload_new.html', {"form": form})

def get_audio_info(request, audio_id):
    audio = get_object_or_404(AudioFile, pk=audio_id)
    return JsonResponse({"file_location": audio.file, "uploaded_date": audio.upload_date})

def analyze_audio_file(request, audio_id):
    audio = get_object_or_404(AudioFile, pk=audio_id)

    if not AudioFeature.objects.filter(pk=audio).exists():
        processAudioFile(audio.file_id)

    if Sentence.objects.filter(pk=audio).exists():
        # getSentenceFromAudio(audio.file_id)
        getWordsFromSentence(audio.file_id)

    return JsonResponse({"file_location": audio.file.path, "uploaded_date": audio.upload_date})