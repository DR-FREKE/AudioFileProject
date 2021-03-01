import os
from Model.audiobook_model import AudiobookModel, audiobook_schema
from .AudioFileOutputter import Outputter
from .AudioInterface import AudioInterface
from flask import jsonify
from Config.database import db
from dataclasses import dataclass
from Config.validation import Validation


@dataclass
class Audiobook(Outputter, AudioInterface):
    requestBody: dict = None

    def insert(self):
        try:
            valid_result = Validation.validateAudiobook(self.requestBody)

            if valid_result['success'] != True:
                return jsonify(valid_result)

            valid_result = valid_result["data"]["metadata"]
            audiobook = AudiobookModel(valid_result)
            db.session.add(audiobook)
            # db.session.flush()
            db.session.commit()
            return self.success(valid_result)

        except Exception as e:
            return jsonify(e)
            # return self.failure("internal server error", 500)

    def remove(self, id):
        try:
            dl_audiobook = db.session.query(
                AudiobookModel).filter_by(id=id).first()

            if not dl_audiobook:
                return self.failure("user does not exist", 400)

            db.session.delete(dl_audiobook)
            db.session.flush()
            audiobook_title = dl_audiobook.title
            db.session.commit()

            return self.success(f"{audiobook_title} has been deleted")
        except Exception as e:
            return self.failure("internal server error", 500)

    def edit(self, id):
        try:
            valid_result = Validation.validateAudiobook(self.requestBody)

            if valid_result['success'] != True:
                return jsonify(valid_result), 400

            valid_result = valid_result["data"]["metadata"]

            ed_audiobook = db.session.query(
                AudiobookModel).filter_by(id=id).first()
            if not ed_audiobook:
                return self.failure("user does not exist", 400)

            ed_audiobook.title = valid_result["name"]
            ed_audiobook.author = valid_result["author"]
            ed_audiobook.narrator = valid_result["narrator"]
            ed_audiobook.duration = valid_result["duration"]

            db.session.add(ed_audiobook)
            db.session.commit()

            return self.success(f"{ed_audiobook.title} has been updated")
        except Exception as e:
            return self.failure("internal server error", 500)

    def readDB(self, id):
        try:
            if id is not None:
                return self.querySpecificAudio(id)
            return self.queryAllAudiobook()
        except Exception as e:
            pass

    def querySpecificAudio(self, id):

        audiobook = db.session.query(AudiobookModel).filter_by(id=id).first()

        if not audiobook:
            return self.failure(f"audiobook with id {id} does not exist", 404)

        response = {"id": audiobook.id, "title": audiobook.title, "author": audiobook.author,
                    "narrator": audiobook.narrator, "duration": audiobook.duration, "uploaded_at": audiobook.uploaded_at}
        return self.success(response)

    def queryAllAudiobook(self):

        audiobook_list = []

        all_audiobook = db.session.query(AudiobookModel).all()

        if len(all_audiobook) <= 0:
            return self.failure("no audiobook found in audiobook table", 400)

        for audiobooks in all_audiobook:
            audiobook_data = {"id": audiobooks.id, "title": audiobooks.title, "author": audiobooks.author,
                              "narrator": audiobooks.narrator, "duration": audiobooks.duration, "uploaded_at": audiobooks.uploaded_at}
            audiobook_list.append(audiobook_data)
        return self.success(audiobook_list)
