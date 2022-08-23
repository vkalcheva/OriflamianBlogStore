from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.review import ReviewManager
from models import UserRole
from schemas.requests.review import ReviewRequestSchema
from schemas.responses.review import ReviewResponseSchema
from utils.decorators import validate_schema, permission_required


class ReviewResource(Resource):
    @auth.login_required
    def get(self):
        user = auth.current_user()
        reviews = ReviewManager.get_reviews(user)
        return ReviewResponseSchema().dump(reviews, many=True)

    @auth.login_required
    @validate_schema(ReviewRequestSchema)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        new_review = ReviewManager.create(data, current_user)
        return ReviewResponseSchema().dump(new_review), 201


class ReviewResourceDetails(Resource):
    @auth.login_required
    @permission_required(UserRole.blogger)
    @validate_schema(ReviewRequestSchema)
    def put(self, id_):
        updated_product = ReviewManager.update(request.get_json(), id_)
        return ReviewResponseSchema().dump(updated_product), 200

    @auth.login_required
    @permission_required(UserRole.blogger)
    def delete(self, id_):
        ReviewManager.delete(id_)
        return {"message": "Success"}, 204