from django.apps import AppConfig
from .models import AudioFile, AudioFeature
import librosa, pickle
import numpy as np


def processAudioFile(audio_id):
    audioFile = AudioFile.objects.get(file_id=audio_id)

    # 모노로 로드 및 샘플레이트 44100Hz로 변경
    data, rate = librosa.core.load(audioFile.file.path, mono=True)

    # 분석
    duration = librosa.get_duration(y=data, sr=rate)

    FFT_SIZE = 4096

    fft_result = librosa.core.stft(data, n_fft=FFT_SIZE)
    freq_magnitude = np.abs(fft_result)
    freq_phase = np.abs(fft_result)

    mfcc = librosa.feature.mfcc(y=data, sr=rate)
    pitch = librosa.feature.chroma_cqt(y=data, sr=rate)
    tempo, frames = librosa.beat.beat_track(y=data, sr=rate)

    # 저장
    audioFeatures = AudioFeature()

    audioFeatures.audio = audioFile

    audioFeatures.mfcc = pickle.dumps(mfcc)
    audioFeatures.pitch = pickle.dumps(pitch)
    audioFeatures.freq_phase = pickle.dumps(freq_phase)
    audioFeatures.freq_magnitude = pickle.dumps(freq_magnitude)

    audioFeatures.tempo = np.asscalar(tempo)

    audioFeatures.save()

class AudiomanagerConfig(AppConfig):
    name = 'audioManager'
