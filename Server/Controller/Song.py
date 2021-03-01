import os
from Model.song_model import SongModel, song_schema
from .AudioFileOutputter import Outputter
from .AudioInterface import AudioInterface
from flask import jsonify
from Config.database import db
from dataclasses import dataclass
from Config.validation import Validation


@dataclass
class Song(Outputter, AudioInterface):
    requestBody: dict = None

    def insert(self):
        try:
            valid_result = Validation.validateSong(self.requestBody)

            if valid_result['success'] != True:
                return jsonify(valid_result)

            valid_result = valid_result["data"]["metadata"]
            song = SongModel(valid_result)
            db.session.add(song)
            # db.session.flush()
            db.session.commit()
            return self.success(valid_result)

        except Exception as e:
            return jsonify(e)

    def remove(self, id):
        try:
            dl_song = db.session.query(
                SongModel).filter_by(id=id).first()

            if not dl_song:
                return self.failure("song does not exist", 400)

            db.session.delete(dl_song)
            db.session.flush()
            song_name = dl_song.name
            db.session.commit()

            return self.success(f"{song_name} has been deleted")
        except Exception as e:
            return jsonify(e)

    def edit(self, id):
        try:
            valid_result = Validation.validateSong(self.requestBody)

            if valid_result['success'] != True:
                return jsonify(valid_result)

            valid_result = valid_result["data"]["metadata"]

            ed_song = db.session.query(
                SongModel).filter_by(id=id).first()
            if not ed_song:
                return self.failure("song does not exist", 400)

            ed_song.name = valid_result["name"]
            ed_song.duration = valid_result["duration"]

            db.session.add(ed_song)
            db.session.commit()

            return self.success(f"{ed_song.name} has been updated")
        except Exception as e:
            return self.failure("internal server error", 500)

    def readDB(self, id):
        try:
            if id is not None:
                return self.querySpecificAudio(id)
            return self.queryAllSongAudio()
        except Exception as e:
            pass

    def querySpecificAudio(self, id):

        song = db.session.query(SongModel).filter_by(id=id).first()

        if not song:
            return self.failure(f"song with id {id} does not exist", 404)

        return self.success({"id": song.id, "name": song.name, "duration": song.duration, "uploaded_at": song.uploaded_at})

    def queryAllSongAudio(self):

        song_list = []

        all_song = db.session.query(SongModel).all()

        if len(all_song) <= 0:
            return self.failure("no song found in song table", 400)

        for songs in all_song:
            song_data = {"id": songs.id, "name": songs.name,
                         "duration": songs.duration, "uploaded_at": songs.uploaded_at}
            song_list.append(song_data)
        return self.success(song_list)
