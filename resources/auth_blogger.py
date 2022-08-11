from flask import request
from flask_restful import Resource
from managers.blogger import BloggerManager
from schemas.requests.blogger import RegisterBloggerRequestSchema, LoginBloggerRequestSchema
from utils.decorators import validate_schema


class RegisterBloggerResource(Resource):
    @validate_schema(RegisterBloggerRequestSchema)
    def post(self):
        data = request.get_json()
        token = BloggerManager.register(data)
        return {"token": token}, 201


class LoginBloggerResource(Resource):
    @validate_schema(LoginBloggerRequestSchema)
    def post(self):
        data = request.get_json()
        token = BloggerManager.login(data)
        return {"token": token}, 200

