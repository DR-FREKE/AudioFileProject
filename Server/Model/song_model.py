import datetime
from Config.database import db, mash


# setup for song model
class SongModel(db.Model):
    __tablename__ = "song"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, data):
        self.name = data["name"]
        self.duration = data["duration"]
        self.uploaded_at = datetime.datetime.now()


# setup song schema
class SongSchema(mash.Schema):
    # create inner class meta
    class Meta:
        fields = ("id", "name", "duration", "uploaded_at")


# instatiate the schema
song_schema = SongSchema()
songs_schema = SongSchema(many=True)
