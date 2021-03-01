from dataclasses import dataclass
from flask import jsonify


@dataclass
class AudioFile:
    audios: list

    def addToDB(self, audio_type):
        try:
            audio = self.checkAudioType(self.audios, audio_type)
            return audio.insert()
        except Exception as e:
            pass

    def deleteFromDB(self, audio_type, id):
        try:
            audio = self.checkAudioType(self.audios, audio_type)
            return audio.remove(id)
        except Exception as e:
            pass

    def updateDB(self, audio_type, id):
        try:
            audio = self.checkAudioType(self.audios, audio_type)
            return audio.edit(id)
        except Exception as e:
            pass

    def readFromDB(self, audio_type, id):
        try:
            audio = self.checkAudioType(self.audios, audio_type)
            return audio.readDB(id)
        except Exception as e:
            pass

    def checkAudioType(self, audios, audio_type):
        for audio in audios:
            class_type = str(type(audio))
            checker = class_type[class_type.index(
                ".", 20)+1:class_type.index("'>")]
            if checker == audio_type:
                return audio
