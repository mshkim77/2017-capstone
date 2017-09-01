from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .forms import FormAddNewAudioFile, FormAddNewAudioFileWithEmotion, FormAddNewAudioFileWithEmotionAndFeatures
from .models import AudioFile, AudioFeature, SampleAudioFeatures
from jobManager.tasks import start_emotion_analysis, extract_audio_features
from jobManager.models import Job
from math import ceil

@csrf_exempt
def record_new_audio(request):
    if request.method == "POST":

        form = FormAddNewAudioFile(request.POST or None, request.FILES or None)

        if form.is_valid():
            job = Job()

            audio_obj = AudioFile()
            audio_obj.file = form.cleaned_data['audio_file']
            audio_obj.save()

            job.status = "AUDIO_FILE_UPLOAD_DONE"
            job.audio = audio_obj
            job.alert_msg = "오디오 파일이 성공적으로 업로드 되었습니다."
            job.save()

            is_saved = True
            audio_id = audio_obj.file_id

            start_emotion_analysis.apply_async((audio_id,))

            return JsonResponse({"saved": is_saved, "job_id": audio_id})

        else:
            return JsonResponse({"saved": False, "job_id": -1})

    else:
        form = FormAddNewAudioFile()
        return render(request, 'audio_record_new.html', {"form": form})

@csrf_exempt
def post_new_audio(request):
    if request.method == "POST":

        form = FormAddNewAudioFile(request.POST or None, request.FILES or None)

        if form.is_valid():
            job = Job()

            audio_obj = AudioFile()
            audio_obj.file = form.cleaned_data['audio_file']
            audio_obj.save()

            job.status = "AUDIO_FILE_UPLOAD_DONE"
            job.audio = audio_obj
            job.alert_msg = "오디오 파일이 성공적으로 업로드 되었습니다."
            job.save()

            is_saved = True
            audio_id = audio_obj.file_id

            start_emotion_analysis.apply_async((audio_id,))

            return JsonResponse({"saved": is_saved, "job_id": audio_id})

        else:
            return render(request, 'audio_post_new.html', {"form": form})

    else:
        form = FormAddNewAudioFile()
        return render(request, 'audio_post_new.html', {"form": form})

def post_new_audio_with_emotions(request):
    if request.method == "POST":

        form = FormAddNewAudioFileWithEmotion(request.POST or None, request.FILES or None)

        if form.is_valid():
            audio_obj = SampleAudioFeatures()
            audio_obj.file = form.cleaned_data['audio_file']
            audio_obj.save()

            # 감정 파싱
            audio_features = SampleAudioFeatures()
            audio_features.audio = audio_obj

            audio_features.rage = form.cleaned_data['rage']
            audio_features.loathing = form.cleaned_data['loathing']
            audio_features.grief = form.cleaned_data['grief']
            audio_features.amazement = form.cleaned_data['amazement']
            audio_features.terror = form.cleaned_data['terror']
            audio_features.admiration = form.cleaned_data['admiration']
            audio_features.ecstasy = form.cleaned_data['ecstasy']
            audio_features.vigilance = form.cleaned_data['vigilance']
            audio_features.have_emotions = True
            audio_features.save()

            # 오디오 분석 리퀘스트 날리기
            extract_audio_features.apply_async((audio_obj.file_id,))

            return render(request, 'audio_upload_new_with_emotions.html', {"form": form, "saved":True})

        else:
            return render(request, 'audio_upload_new_with_emotions.html', {"form": form})

    else:
        form = FormAddNewAudioFileWithEmotion()
        return render(request, 'audio_upload_new_with_emotions.html', {"form": form})

@csrf_exempt
def post_new_audio_with_emotions_and_features(request):
    if request.method == "POST":

        form = FormAddNewAudioFileWithEmotionAndFeatures(request.POST or None, request.FILES or None)

        if form.is_valid():
            audio_features = SampleAudioFeatures()

            if form.cleaned_data['audio_file']:
                audio_obj = AudioFile()
                audio_obj.file = form.cleaned_data['audio_file']
                audio_obj.save()

                audio_features.audio = audio_obj

            # 특징 파싱
            audio_features.duration = form.cleaned_data['duration']
            audio_features.tempo = form.cleaned_data['tempo']

            audio_features.avg_mfcc = form.cleaned_data['avg_mfcc']
            audio_features.max_mfcc = form.cleaned_data['max_mfcc']
            audio_features.min_mfcc = form.cleaned_data['min_mfcc']
            audio_features.var_mfcc = form.cleaned_data['var_mfcc']
            audio_features.std_mfcc = form.cleaned_data['std_mfcc']

            audio_features.avg_ZCR = form.cleaned_data['avg_ZCR']
            audio_features.var_ZCR = form.cleaned_data['var_ZCR']
            audio_features.std_ZCR = form.cleaned_data['std_ZCR']

            audio_features.avg_energy = form.cleaned_data['avg_energy']
            audio_features.max_energy = form.cleaned_data['max_energy']
            audio_features.min_energy = form.cleaned_data['min_energy']
            audio_features.std_energy = form.cleaned_data['std_energy']

            audio_features.avg_harmonic = form.cleaned_data['avg_harmonic']
            audio_features.avg_harmonic_in_max = form.cleaned_data['avg_harmonic_in_max']
            audio_features.avg_harmonic_in_min = form.cleaned_data['avg_harmonic_in_min']

            audio_features.diff_avg_harmonic_max = form.cleaned_data['diff_avg_harmonic_max']
            audio_features.diff_avg_harmonic_min = form.cleaned_data['diff_avg_harmonic_min']
            audio_features.diff_avg_harmonic_maxmin = form.cleaned_data['diff_avg_harmonic_maxmin']

            # 감정 파싱
            audio_features.rage = form.cleaned_data['rage']
            audio_features.loathing = form.cleaned_data['loathing']
            audio_features.grief = form.cleaned_data['grief']
            audio_features.amazement = form.cleaned_data['amazement']
            audio_features.terror = form.cleaned_data['terror']
            audio_features.admiration = form.cleaned_data['admiration']
            audio_features.ecstasy = form.cleaned_data['ecstasy']
            audio_features.vigilance = form.cleaned_data['vigilance']
            audio_features.have_emotions = True

            audio_features.save()

            return JsonResponse({"status": "true", })
            # return render(request, 'audio_upload_new_with_emotions_and_features.html', {"form": form, "saved":True})

        else:
            return JsonResponse({"status": "false", })
            # return render(request, 'audio_upload_new_with_emotions_and_features.html', {"form": form})

    else:
        form = FormAddNewAudioFileWithEmotionAndFeatures()
        return render(request, 'audio_upload_new_with_emotions_and_features.html', {"form": form})

def get_audio_info(request, audio_id):
    audio_obj = get_object_or_404(AudioFile, pk=audio_id)
    features = get_object_or_404(AudioFeature, pk=audio_obj)
    features_data = model_to_dict(features)

    result_data = {}
    emotion_keys = ["rage", "vigilance", "ecstasy", "admiration", "amazement", "terror", "grief", "loathing"]

    for key in emotion_keys:
        result_data.update({key: ceil(features_data[key] * 100)})

    result_data.update({"aggressiveness": ceil((features_data["rage"] + features_data["vigilance"]) / 2)})
    result_data.update({"optimistic": ceil((features_data["vigilance"] + features_data["ecstasy"]) / 2)})
    result_data.update({"love": ceil((features_data["ecstasy"] + features_data["admiration"]) / 2)})
    result_data.update({"submission": ceil((features_data["admiration"] + features_data["terror"]) / 2)})
    result_data.update({"awe": ceil((features_data["terror"] + features_data["amazement"]) / 2)})
    result_data.update({"disapproval": ceil((features_data["amazement"] + features_data["grief"]) / 2)})
    result_data.update({"remorse": ceil((features_data["grief"] + features_data["loathing"]) / 2)})
    result_data.update({"contempt": ceil((features_data["loathing"] + features_data["rage"]) / 2)})

    return render(request, 'show_result.html', {"audio_data": result_data})

def analyze_audio_file(request, audio_id):
    if AudioFile.objects.filter(pk=audio_id).exists():
        start_emotion_analysis.apply_async((audio_id,))
        return JsonResponse({"job_id": audio_id, "status": "ok",})
    else:
        return JsonResponse({"job_id": -1, "status": "error",})
