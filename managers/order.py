from collections import Counter

from flask import request
from werkzeug.exceptions import BadRequest

from db import db

from models import ProductModel, OrderModel, ProductsInOrder, State


class OrderManager:
    @staticmethod
    def create(data, user, card_token):
        data = request.get_json()
        data["blogger_id"] = user.id

        products = []
        product_id_quantities = Counter(data["products"])

        for _id, count in product_id_quantities.most_common():
            product = ProductModel.query.filter_by(id=_id).first()
            if not product:
                return BadRequest
            products.append(ProductsInOrder(product_id=_id, quantity=count))

        order = OrderModel(products=products, blogger_id=user.id, status=State.approved)

        db.session.add(order)
        db.session.commit()
        order.create_payment_charge(card_token)

        return order

    @staticmethod
    def approve(order_id):
        OrderModel.query.filter_by(id=order_id).update({"status": State.approved})

    @staticmethod
    def reject(order_id):
        OrderModel.query.filter_by(id=order_id).update({"status": State.rejected})
