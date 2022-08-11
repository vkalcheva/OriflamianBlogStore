from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.post import PostManager
from schemas.requests.post import PostRequestSchema
from schemas.responses.post import PostResponseSchema
from utils.decorators import validate_schema


class PostResource(Resource):
    @auth.login_required
    @validate_schema(PostRequestSchema)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        new_post = PostManager.create(data, current_user)
        return PostResponseSchema().dump(new_post), 201