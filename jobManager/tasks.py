import capstone2017.settings as settings
from capstone2017.celery import app as celery_app

from audioManager.models import AudioFile

from audioManager.apps import processAudioFile, do_extract_feature
from sentenceManager.apps import get_sentence_from_audio
from wordManager.apps import get_words_from_sentence
from tensorManager.apps import knn_tone_emotion_analysis

from .models import Job

@celery_app.task()
def start_emotion_analysis(audio_id):
    audio_obj = AudioFile(pk=audio_id)
    job = Job()

    if Job.objects.filter(pk=audio_obj).exists():
        job = Job.objects.get(pk=audio_obj)

    print("특징 추출중")
    update_job_status(job, "AUDIO_FILE_PROCESSING", "오디오 파일을 전처리하고 있습니다.")
    processAudioFile(audio_id)
    audio_obj.refresh_from_db()

    print("특징 추출중")
    update_job_status(job, "AUDIO_FEATURE_EXTRACTING", "오디오 파형의 특징을 추출하고 있습니다.")
    if not do_extract_feature(audio_id):
        update_job_status(job, "ERROR", "특징을 추출할 수 없습니다!")
        return

    print("STT 작업 중")
    update_job_status(job, "AUDIO_SENTENCE_EXTRACTING", "음성파일을 문자열로 변환하고 있습니다.")
    #if not get_sentence_from_audio(audio_id):
    #    update_job_status(job, "ERROR", "STT 작업을 완료할 수 없습니다!")

    print("단어 추출 중")
    update_job_status(job, "SENTENCE_WORD_EXTRACTING", "문자열로 부터 단어를 추출하고 있습니다.")
    #if not get_words_from_sentence(audio_id):
    #    update_job_status(job, "ERROR_WORD_EXTRACTING", "문장에서 단어를 추출할 수 없습니다!")

    print("톤 분석중")
    update_job_status(job, "EMOTION_PREDICTING", "감정을 분석하고 있습니다.")
    if not knn_tone_emotion_analysis(audio_id):
        update_job_status(job, "ERROR", "샘플 데이터가 적어서 분석을 완료할 수 없습니다!")
        return

    update_job_status(job, "DONE", "완료")

@celery_app.task()
def extract_audio_features(audio_id):
    audio_obj = AudioFile(pk=audio_id)
    job = Job()

    if not Job.objects.filter(pk=audio_obj).exists():
        update_job_status(job, "AUDIO_FILE_PROCESSING")
        processAudioFile(audio_id)

        audio_obj.refresh_from_db()

        update_job_status(job, "AUDIO_FEATURE_EXTRACTING")
        do_extract_feature(audio_id)

        update_job_status(job, "DONE")

def update_job_status(job, status, msg=""):
    job.status = status
    job.alert_msg = msg
    job.save()





