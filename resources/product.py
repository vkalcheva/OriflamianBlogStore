from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.product import ProductManager
from models import UserRole
from schemas.requests.product import ProductRequestSchema
from schemas.responses.product import ProductResponseSchema
from utils.decorators import permission_required, validate_schema


class ProductResource(Resource):
    #test with blogger token
    @auth.login_required
    @permission_required(UserRole.admin)
    def get(self):
        products = ProductManager.get_all()
        return ProductResponseSchema().dump(products, many=True), 200

    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(ProductRequestSchema)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        new_product = ProductManager.create(data, current_user)
        return ProductResponseSchema().dump(new_product), 201



