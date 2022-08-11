from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.category import CategoryManager
from models import UserRole
from schemas.requests.category import CategoryRequestSchema
from schemas.responses.category import CategoryResponseSchema
from utils.decorators import permission_required, validate_schema


class CategoryResource(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(CategoryRequestSchema)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        new_category = CategoryManager.create(data, current_user)
        return CategoryResponseSchema().dump(new_category), 201

