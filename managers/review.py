from werkzeug.exceptions import NotFound

from db import db
from managers.auth import auth
from models import ReviewModel, UserRole


class ReviewManager:
    @staticmethod
    def get_reviews(user):
        if user.role == UserRole.blogger:
            return ReviewModel.query.filter_by(blogger_id=user.id).all()
        return ReviewModel.query.all()

    @staticmethod
    def create(data, user):
        data["blogger_id"] = user.id
        review = ReviewModel(**data)
        db.session.add(review)
        db.session.flush()
        return review

    @staticmethod
    def update(review_data, id_):
        review_obj_query = ReviewModel.query.filter_by(id=id_)
        review = review_obj_query.first()
        if not review:
            raise NotFound("This review does not exist")
        blogger = auth.current_user()

        if not blogger.id == review.blogger_id:
            raise NotFound("This review could not be changed")

        review_obj_query.update(review_data)
        db.session.add(review)
        db.session.flush()
        return review

    @staticmethod
    def delete(id_):
        review_obj_query = ReviewModel.query.filter_by(id=id_)
        review = review_obj_query.first()
        if not review:
            raise NotFound("This review does not exist")
        blogger = auth.current_user()

        if not blogger.id == review.blogger_id:
            raise NotFound("This review could not be deleted")

        db.session.delete(review)
        db.session.flush()
