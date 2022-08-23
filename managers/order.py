from collections import Counter

from flask import request
from werkzeug.exceptions import BadRequest, NotFound

from db import db
from models import ProductModel, OrderModel, ProductsInOrder, State


class OrderManager:
    def create(self, user):
        data = request.get_json()
        data["blogger_id"] = user.id

        products = []
        product_id_quantities = Counter(data["products"])

        for _id, count in product_id_quantities.most_common():
            product = ProductModel.query.filter_by(id=_id).first()
            if not product:
                return BadRequest
            products.append(ProductsInOrder(product_id=_id, quantity=count))

        order = OrderModel(products=products, blogger_id=user.id)

        db.session.add(order)
        db.session.flush()
        return order

    @staticmethod
    def approve(id_, card_token):
        order_q = OrderModel.query.filter_by(id=id_)
        order = order_q.first()
        if not order:
            raise NotFound("This order does not exist")
        order_q.update({"status": State.approved})
        db.session.add(order)
        db.session.flush()
        order.create_payment_charge(card_token)
        return order

    @staticmethod
    def reject(id_):
        order_q = OrderModel.query.filter_by(id=id_)
        order = order_q.first()
        if not order:
            raise NotFound("This order does not exist")
        order_q.update({"status": State.rejected})
        db.session.add(order)
        db.session.flush()
        return order
