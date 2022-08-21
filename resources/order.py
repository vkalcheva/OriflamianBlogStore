from flask import request
from flask_restful import Resource

from services.stripe import StripeService

from managers.auth import auth
from managers.order import OrderManager
from models import UserRole
from schemas.requests.order import OrderSchemaRequest
from schemas.responses.order import OrderSchemaResponse
from utils.decorators import validate_schema, permission_required

stripe_service = StripeService()


class OrderResource(Resource):
    @auth.login_required
    @permission_required(UserRole.blogger)
    @validate_schema(OrderSchemaRequest)
    def post(self):
        data = request.get_json()
        card_token = stripe_service.create_card()
        current_user = auth.current_user()

        new_order = OrderManager.create(data, current_user, card_token)

        return OrderSchemaResponse().dump(new_order), 201


class ApproveOrderResource(Resource):
    @auth.login_required
    def put(self, id):
        OrderManager.approve(id)
        return 204


class RejectOrderResource(Resource):
    @auth.login_required
    def put(self, id):
        OrderManager.reject(id)
        return 204
