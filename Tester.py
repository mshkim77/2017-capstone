import pymongo

from pymongo import MongoClient

class MongoDB_Module :
    client = MongoClient()

    db = client.capstone # capstone db 사용

    def insert_speechToStr(audio_file_name, speechToStr):
        myrecord = {
            'file_name': audio_file_name,
            "Speech_to_Str" : speechToStr
        }
        db.emotionObjects.insert(myrecord) #emotionObjects collection에 삽입

    #db.emotionObjects.update({'speech_t':10},{'$set':{'speech_weight':10}})




MongoDB_Module.insert_speechToStr('tester file','hi there')