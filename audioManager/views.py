from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .forms import FormAddNewAudioFile
from .models import AudioFile
from jobManager.tasks import start_emotion_analysis

@csrf_exempt
def post_new_audio(request):
    if request.method == "POST":

        form = FormAddNewAudioFile(request.POST or None, request.FILES or None)

        if form.is_valid():
            print("Hello!")
            audioFile = AudioFile()
            audioFile.file = form.cleaned_data['audio_file']
            audioFile.save()

            isSaved = True
            fileID = audioFile.file_id

            return JsonResponse({"saved": isSaved, "job_id": fileID})

        else:
            return JsonResponse({"saved": False, "job_id": -1})
            # raise Http404

    else:
        form = FormAddNewAudioFile()
        return render(request, 'audio_upload_new.html', {"form": form})

def get_audio_info(request, audio_id):
    audio = get_object_or_404(AudioFile, pk=audio_id)
    return JsonResponse({"file_location": audio.file, "uploaded_date": audio.upload_date})

def analyze_audio_file(request, audio_id):
    if AudioFile.objects.filter(pk=audio_id).exists():
        start_emotion_analysis(audio_id)
        return JsonResponse({"job_id": audio_id, "status": "ok",})
    else:
        return JsonResponse({"job_id": -1, "status": "error",})