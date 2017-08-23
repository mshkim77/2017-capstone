from audioManager.models import AudioFile
from .models import Sentence
import capstone2017.settings as settings
import speech_recognition as sr

def get_sentence_from_audio(audio_id):
    # 오디오 파일 로드
    audio_obj = AudioFile.objects.get(file_id=audio_id)

    # 구글 TTS 초기화
    recognizer = sr.Recognizer()
    path = audio_obj.file.path

    # 변환 된 파일이 있는지 확인 (있다 = wav, 없다 = 이미 파일이 wav)
    if audio_obj.converted_file is not None:
        path = audio_obj.converted_file.path

    with sr.AudioFile(path) as source:
        # 문장 객체 초기화
        sentence = Sentence()
        sentence.audioFile = audio_obj

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

        return sentence





