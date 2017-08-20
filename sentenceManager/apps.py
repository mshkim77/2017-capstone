from audioManager.models import AudioFile
from .models import Sentence
import capstone2017.settings as settings
import speech_recognition as sr

def getSentenceFromAudio(audio_id):
    # 오디오 파일 로드
    audioFile = AudioFile.objects.get(file_id=audio_id)

    # 구글 TTS 초기화
    recognizer = sr.Recognizer()

    with sr.AudioFile(audioFile.file.path) as source:
        # 문장 객체 초기화
        sentence = Sentence()
        sentence.audioFile = audioFile

        # 오디오 생성 (전송할 것)
        audio = recognizer.record(source)

        try:
            # 전송
            stt_results = recognizer.recognize_google_cloud(audio,
                                                            credentials_json=settings.GOOGLE_CLOUD_SPEECH_CREDENTIALS,
                                                            language="ko-KR")

            # 결과를 문장 객체에 대입
            sentence.sentence = stt_results
            sentence.hasError = False
            sentence.reliability = 1.0

        except sr.UnknownValueError:
            sentence.sentence = ""
            sentence.hasError = True
            sentence.reliability = 0.0

        except sr.RequestError:
            sentence.sentence = ""
            sentence.hasError = True
            sentence.reliability = 0.0

        # 문장 객체 저장
        sentence.save()





