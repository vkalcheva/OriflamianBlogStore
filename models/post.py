from sqlalchemy import func

from db import db


class PostModel(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullbull=False)
    photo_url = db.Column(db.String(255), nullbull=False)
    description = db.Column(db.Text, nullbull=False)
    date_created = db.Column(db.DateTime, server_default=func.now())

    blogger_id = db.Column(db.Integer, db.ForeignKey("bloggers.id"))
    blogger = db.relationship("BloggerModel")
