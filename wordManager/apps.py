from django.apps import AppConfig

from audioManager.models import AudioFile
from sentenceManager.models import Sentence
from konlpy.tag import Twitter
from .models import Word

def get_words_from_sentence(audio_id):
    # 오디오 파일 및 문장 로드
    audioFile = AudioFile.objects.get(file_id=audio_id)
    sentence = Sentence.objects.get(pk=audioFile)

    # 문장에 오류가 없을 때만 실행
    if not sentence.hasError:
        tagger = Twitter()
        result = tagger.pos(sentence.sentence)
        result = ['/'.join(t) for t in result]

        for w in result:
            if not Word.objects.filter(word=w).exists():
                word = Word()
                word.word = w
                word.save()

            sentence.words.add(Word.objects.get(word=w))

        sentence.save()

    return sentence

class wordManagerConfig(AppConfig):
    name = 'wordManager'
