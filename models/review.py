# from sqlalchemy import func
#
# from db import db
#
#
# class ReviewModel(db.Model):
#     __tablename__ = "reviews"
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     comment = db.Column(db.Text, nullable=False)
#     post_date = db.Column(db.DateTime, server_default=func.now())
#
#     blogger_id = db.Column(db.Integer, db.ForeignKey("bloggers.id"))
#     blogger = db.relationship("BloggerModel")
#
#     post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
#     post = db.relationship("PostModel")
#
