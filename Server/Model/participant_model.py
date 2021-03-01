import datetime
from Config.database import db, mash


# setup participant model
class ParticipantModel(db.Model):
    __tablename__ = "participant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    podcast_id = db.Column(db.Integer, db.ForeignKey("podcast.id"))
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, podcast_id):
        self.name = name
        self.podcast_id = podcast_id
        self.created_at = datetime.datetime.now()


# setup participant schema
class ParticipantSchema(mash.Schema):
    # create inner class meta
    class Meta:
        fields = ("id", "name", "podcast_id", "created_at")


# instantiate schema
participant_schema = ParticipantSchema()
particupants_schema = ParticipantSchema(many=True)
