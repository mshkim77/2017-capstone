import pymongo

from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDB_Module :

    __client = 0
    __db = 0

    #DB 연결 및 사용 DB 설정
    def DBconnetion(self):
        self.__client = MongoClient()
        self.__db = self.__client.capstone



    def insert_Mongo_emotionValues(self, myrecord):
        self.__db.emotionValues.insert(myrecord)

    def get_Mongo_emotionValues(self, audio_file_name):
        docs = self.__db.emotionValues.find({"audio_file_name":audio_file_name})
        print(docs)
        for i in docs:
            print(i)

    # ALG1 파일 이름, STT 결과 문자열 저장
    def insert_speechToStr(self, audio_file_name, speechToStr):
        myrecord = {
            'file_id': audio_file_name,
            "Speech_to_Str" : speechToStr
        }
        self.__db.emotionObjects.insert(myrecord) #emotionObjects collection에 삽입

    def insert_speechToStr1(self, myrecord):
        self.__db.emotionObjects.insert(myrecord) #emotionObjects collection에 삽입


    # 문장에 대한 감정(배열) 저장
    def insert_emotions(self, audio_file_name, emotions):
        self.db.emotionObjects.update({'file_id':audio_file_name},{'$set':{'emotions':emotions}})

    # ALG2 톤에 대한 가중치 저장
    def insert_weights(self, audio_file_name, tone_weight):
        self.db.emotionObjects.update({'file_id':audio_file_name},{'$set':{'tone_weight':tone_weight}})

    # ALG3 말속도 가중치 저장
    def insert_weights(self, audio_file_name, speech_speed_weight):
        self.db.emotionObjects.update({'file_id':audio_file_name},{'$set':{'speech_speed':speech_speed_weight}})

    # ALG4 문장에서 감정명사당 가중치(배열 : [감정단어, 가중치],...) 저장
    def insert_emotionWord_per_weight(self, audio_file_name, emotionWords_weigh):
        #for (emotionWord, weight) in emotions:
        self.db.emotionObjects.update({'file_id': 'tester file'},
                                      {'$push':{'emotionWord_per_weight': {'$each': emotionWords_weigh }}})

    def select_speechToStr(self, file_id):
        docs = self.db.emotionObjects.find({'file_id':file_id})
        print(docs)

    #wordManager
    def insert_wordManger(self, word, rage, loathing, grief, amazement, terror, admiration, ecstasy, vigilance):
        record = {
            'word_id':word,
            'rage':rage, 'loathing':loathing , 'grief':grief, 'amazement':amazement,
                     'terror':terror, 'admiration':admiration, 'ecstasy': ecstasy, 'vigilance':vigilance
        }
        self.db.wordManager.insert(record)

    def get(self, post_id):
        document = self.db.emotionObjects.find_one({'_id':ObjectId(post_id)})
        print(document)