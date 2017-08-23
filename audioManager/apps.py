from django.apps import AppConfig
from .models import AudioFile
from pydub import AudioSegment
import os, codecs
import capstone2017.settings as settings
from django.core.files import File

def processAudioFile(audio_id):
    audio_obj = AudioFile.objects.get(file_id=audio_id)
    path_component = str(audio_obj.file.path).split(os.sep)
    file_name = path_component[-1].split(".")[0]
    file_ext = path_component[-1].split(".")[1]

    if not file_ext == "wav":
        AudioSegment.converter = settings.FFMPEG_LOC
        audio = AudioSegment.from_file(audio_obj.file.path, file_ext)
        tmp_dir = settings.MEDIA_ROOT + os.sep + "temp"
        tmp_loc = tmp_dir + os.sep + file_name + ".wav"
        print(tmp_loc)

        audio.export(tmp_loc, format="wav")

        with codecs.open(tmp_loc, "r", encoding='utf-8', errors='ignore') as f_data:
            audio_obj.converted_file.save("converted.wav", File(f_data))

        audio_obj.save()

        os.remove(tmp_loc)

class AudiomanagerConfig(AppConfig):
    name = 'audioManager'
