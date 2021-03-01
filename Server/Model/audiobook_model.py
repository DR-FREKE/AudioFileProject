import datetime
from Config.database import db, mash


# setup podcast model
class AudiobookModel(db.Model):
    __tablename__ = "audiobook"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, data):
        self.title = data["title"]
        self.author = data["author"]
        self.narrator = data["narrator"]
        self.duration = data["duration"]
        self.uploaded_at = datetime.datetime.now()


# setup podcast schema
class AudiobookSchema(mash.Schema):
    # create inner class meta
    class Meta:
        fields = ("id", "title", "author", "narrator",
                  "duration", "uploaded_at")


# instantiate schema
audiobook_schema = AudiobookSchema()
audiobooks_schema = AudiobookSchema(many=True)
