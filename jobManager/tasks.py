import capstone2017.settings as settings
from capstone2017.celery import app as celery_app

from audioManager.models import AudioFile

from audioManager.apps import processAudioFile, do_extract_feature
from sentenceManager.apps import get_sentence_from_audio
from wordManager.apps import get_words_from_sentence

from .models import Job


@celery_app.task()
def start_emotion_analysis(audio_id):
    audio_obj = AudioFile(pk=audio_id)
    job = Job()

    if not Job.objects.filter(pk=audio_obj).exists():
        update_job_status(job, "AUDIO_FILE_PROCESSING")
        processAudioFile(audio_id)

        audio_obj.refresh_from_db()

        update_job_status(job, "AUDIO_FEATURE_EXTRACTING")
        feature = do_extract_feature(audio_id)

        update_job_status(job, "AUDIO_SENTENCE_EXTRACTING")
        sentence = get_sentence_from_audio(audio_id)

        update_job_status(job, "SENTENCE_WORD_EXTRACTING")
        sentence = get_words_from_sentence(audio_id)


def update_job_status(job, status):
    job.status = status
    job.save()





