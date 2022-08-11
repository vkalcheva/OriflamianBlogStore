from sqlalchemy import func

from db import db


class PostModel(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, server_default=func.now())

    blogger_id = db.Column(db.Integer, db.ForeignKey("bloggers.id"), nullable=False)
    blogger = db.relationship("BloggerModel")
