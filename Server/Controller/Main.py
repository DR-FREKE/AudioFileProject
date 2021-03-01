from Controller.Song import Song
from Controller.Podcast import Podcast
from Controller.Audiobook import Audiobook
from Controller.AudioFile import AudioFile
from Controller.AudioFileOutputter import Outputter
from flask import request, jsonify
from dataclasses import dataclass


@dataclass
class Main(Outputter):
    # private variable holding a tuple
    __enum_type = ("Song", "Podcast", "Audiobook")

    def add(self):
        try:
            requestBody = request.json

            if requestBody['audiotype'] not in Main.__enum_type:
                return self.message()

            all_audio = [Song(requestBody), Podcast(
                requestBody), Audiobook(requestBody)]
            action = AudioFile(all_audio)

            return action.addToDB(requestBody["audiotype"])
        except Exception as e:
            return self.failure("internal server error", 500)

    def delete(self, audio_type, id):
        try:

            if audio_type not in Main.__enum_type:
                return self.message()

            all_audio = [Song(), Podcast(), Audiobook()]
            action = AudioFile(all_audio)

            return action.deleteFromDB(audio_type, id)
        except Exception as e:
            return self.failure(f"internal server error {e}", 500)

    def update(self, audio_type, id):
        try:
            requestBody = request.json

            if audio_type not in Main.__enum_type:
                return self.message()

            all_audio = [Song(requestBody), Podcast(
                requestBody), Audiobook(requestBody)]
            action = AudioFile(all_audio)

            return action.updateDB(audio_type, id)

        except Exception as e:
            return self.failure(f"internal server error {e}", 500)

    def read(self, audio_type, id):
        try:
            if audio_type not in Main.__enum_type:
                return self.message()

            all_audio = [Song(), Podcast(), Audiobook()]
            action = AudioFile(all_audio)

            return action.readFromDB(audio_type, id)

        except Exception as e:
            return self.failure(f"internal server error", 500)

    def message(self):
        return self.failure(f"type must be one of {Main.__enum_type}", 400)
