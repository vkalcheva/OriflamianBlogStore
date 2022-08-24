from flask import request
from flask_restful import Resource

from managers.admin import AdminManager
from schemas.requests.admin import LoginAdminRequestSchema, RegisterAdminRequestSchema
from utils.decorators import validate_schema


class RegisterAdminResource(Resource):
    @validate_schema(RegisterAdminRequestSchema)
    def post(self):
        data = request.get_json()
        token = AdminManager.register(data)
        return {"token": token}, 201


class LoginAdminResource(Resource):
    @validate_schema(LoginAdminRequestSchema)
    def post(self):
        data = request.get_json()
        token = AdminManager.login(data)
        return {"token": token}, 200
