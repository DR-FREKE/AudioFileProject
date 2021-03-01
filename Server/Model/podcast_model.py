import datetime
from Config.database import db, mash


# setup podcast model
class PodcastModel(db.Model):
    __tablename__ = "podcast"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    host = db.Column(db.String(100), nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False)
    participant = db.relationship(
        "ParticipantModel", backref="podcast", lazy=True)

    def __init__(self, data):
        self.name = data["name"]
        self.duration = data["duration"]
        self.host = data["host"]
        self.uploaded_at = datetime.datetime.now()


# setup podcast schema
class PodcastSchema(mash.Schema):
    # create inner class meta
    class Meta:
        fields = ("id", "name", "duration", "host", "uploaded_at")


# instantiate schema
podcast_schema = PodcastSchema()
podcasts_schema = PodcastSchema(many=True)
