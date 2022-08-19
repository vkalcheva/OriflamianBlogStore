from db import db
from models import ReviewModel


class ReviewManager:
    @staticmethod
    def create(data, user):
        data["blogger_id"] = user.id
        review = ReviewModel(**data)
        db.session.add(review)
        db.session.flush()
        return review

