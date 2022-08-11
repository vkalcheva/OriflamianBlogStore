from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.review import ReviewManager
from schemas.requests.review import ReviewRequestSchema
from schemas.responses.review import ReviewResponseSchema
from utils.decorators import validate_schema


class ReviewResource(Resource):
    @auth.login_required
    @validate_schema(ReviewRequestSchema)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        new_review = ReviewManager.create(data, current_user)
        return ReviewResponseSchema().dump(new_review), 201