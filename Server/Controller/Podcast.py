import os
from Model.podcast_model import PodcastModel, podcast_schema
from Model.participant_model import ParticipantModel, participant_schema
from .AudioFileOutputter import Outputter
from .AudioInterface import AudioInterface
from flask import jsonify
from Config.database import db
from dataclasses import dataclass
from Config.validation import Validation


@dataclass
class Podcast(Outputter, AudioInterface):
    requestBody: dict = None

    def insert(self):
        try:
            valid_result = Validation.validatePodcast(self.requestBody)

            if valid_result['success'] != True:
                return jsonify(valid_result)

            valid_result = valid_result["data"]["metadata"]
            podcast = PodcastModel(valid_result)
            db.session.add(podcast)
            db.session.flush()

            if valid_result["participants"]:
                valid_result["podcast_id"] = podcast.id
                self.addParticipant(valid_result)

            db.session.commit()

            return self.success(valid_result)

        except Exception as e:
            print(e)
            return jsonify(e)

    def addParticipant(self, data):
        podcast_id = data["podcast_id"]
        participants = data["participants"]

        for particapant in participants:
            participant_exist = db.session.query(
                ParticipantModel).filter_by(name=particapant).first()

            if not participant_exist:
                pd_participant = ParticipantModel(particapant, podcast_id)
                db.session.add(pd_participant)
                db.session.commit()

    def remove(self, id):
        try:
            dl_podcast = db.session.query(
                PodcastModel).filter_by(id=id).first()

            if not dl_podcast:
                return jsonify("user does not exist")

            dl_participant = db.session.query(
                ParticipantModel).filter_by(podcast_id=dl_podcast.id).all()

            if dl_participant:

                for participant in dl_participant:
                    db.session.delete(participant)
                    db.session.commit()

            db.session.delete(dl_podcast)
            db.session.flush()
            pod_name = dl_podcast.name
            db.session.commit()

            return self.success(f"{pod_name} has been deleted")

        except Exception as e:
            return jsonify(e)

    def edit(self, id):
        try:
            valid_result = Validation.validatePodcast(self.requestBody)

            if valid_result['success'] != True:
                return jsonify(valid_result)

            valid_result = valid_result["data"]["metadata"]

            ed_podcast = db.session.query(
                PodcastModel).filter_by(id=id).first()
            if not ed_podcast:
                return self.failure("user does not exist", 400)

            if valid_result["participants"]:
                valid_result["podcast_id"] = ed_podcast.id
                self.addParticipant(valid_result)
            ed_podcast.name = valid_result["name"]
            ed_podcast.host = valid_result["host"]
            ed_podcast.duration = valid_result["duration"]
            db.session.add(ed_podcast)
            db.session.commit()

            return self.success(f"{ed_podcast.name} has been updated")
        except Exception as e:
            return jsonify(e)

    def readDB(self, id):
        try:
            if id is not None:
                return self.querySpecificAudio(id)
            return self.queryAllPodcastAudio()
        except Exception as e:
            pass

    def querySpecificAudio(self, id):

        podcast = db.session.query(PodcastModel).filter_by(id=id).first()

        if not podcast:
            return self.failure(f"podcast with id {id} does not exist", 404)

        participants = self.getParticipants(id)

        response = {"id": podcast.id, "name": podcast.name, "duration": podcast.duration,
                    "host": podcast.host, "uploaded_at": podcast.uploaded_at, "participants": participants}
        return self.success(response)

    def queryAllPodcastAudio(self):

        podcast_list = []

        all_podcast = db.session.query(PodcastModel).all()

        if len(all_podcast) <= 0:
            return self.failure("no podcast found in podcast table", 400)

        for podcasts in all_podcast:
            participants = self.getParticipants(podcasts.id)
            podcast_data = {"id": podcasts.id, "name": podcasts.name, "host": podcasts.host,
                            "duration": podcasts.duration, "participants": participants, "uploaded_at": podcasts.uploaded_at}
            podcast_list.append(podcast_data)
        return self.success(podcast_list)

    def getParticipants(self, id):
        participant_list = []

        participants = db.session.query(
            ParticipantModel).filter_by(podcast_id=id).all()

        if len(participants) <= 0:
            return
        for all_participant in participants:
            participant_list.append(all_participant.name)

        return participant_list
