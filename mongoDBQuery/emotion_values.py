from mongoDBQuery.mongoQuery import MongoDB_Module

class emotion_values(object):

    mongo = MongoDB_Module()
    mongo.DBconnetion()

    def __int__(self):
        self.__audio_file_name = ""
        self.__rage = 0
        self.__loathing = 0
        self.__grief = 0
        self.__amazement = 0
        self.__terror = 0
        self.__admiration = 0
        self.__ecstasy = 0
        self.__vigilance = 0

    #8개 감정 0~1 가중치 배열로 받음
    def insert_emotionValues(self, audio_file_name, emotionValues):

        if emotion_values.checkValue(self, emotionValues)!=0:
            self.__audio_file_name = audio_file_name

            self.__rage = emotionValues[0]
            self.__loathing = emotionValues[1]
            self.__grief = emotionValues[2]
            self.__amazement = emotionValues[3]
            self.__terror = emotionValues[4]
            self.__admiration = emotionValues[5]
            self.__ecstasy = emotionValues[6]
            self.__vigilance = emotionValues[7]
            print("vaild value")
        else:
            print("invaild value")

    def get_emotionValues(self, audio_file_name):
        self.mongo.get_Mongo_emotionValues(audio_file_name)

    def save(self):
        myrecord = {
            "audio_file_name": self.__audio_file_name,
            "rage": self.__rage,
            "loathing": self.__loathing,
            "grief": self.__grief,
            "amazement": self.__amazement,
            "terror": self.__terror,
            "admiration": self.__admiration,
            "ecstasy": self.__ecstasy,
            "vigilance": self.__vigilance
        }
        self.mongo.insert_Mongo_emotionValues(myrecord)

    #데이터 유효성 검사
    def checkValue(self, emotionValues):
        for emotions in emotionValues:
            if 0 < emotions and emotions > 1:
                return 0

    def returnValue(self):
        print(self.__grief)



