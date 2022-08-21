import stripe
from sqlalchemy import func

from db import db
from models.enums import State


class ProductsInOrder(db.Model):
    __tablename__ = "products_in_order"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    quantity = db.Column(db.Integer)

    product = db.relationship("ProductModel")
    order = db.relationship("OrderModel", back_populates="products")


class OrderModel(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    status = db.Column(db.Enum(State), default=State.pending, nullable=False)

    blogger_id = db.Column(db.Integer, db.ForeignKey("bloggers.id"))
    blogger = db.relationship("BloggerModel")

    products = db.relationship("ProductsInOrder", back_populates="order")

    @property
    def description(self) -> str:
        """
        Generates a simple string representing this order, in the format of "5x chair, 2x table"
        """
        product_counts = [f"{product_data.quantity}x {product_data.product.name}" for product_data in self.products]
        return ",".join(product_counts)

    @property
    def amount(self) -> int:
        """
        Calculates the total amount to charge for this order.
        Assumes item price is in USD–multi-currency becomes much tricker!
        :return int: total amount of cents to be charged in this order.x`
        """
        return int(sum([product_data.product.price * product_data.quantity for product_data in self.products]) * 100)

    def generate_card_token(self):
        data = stripe.Token.create(
            card={
                "number": "4242424242424242",
                "exp_month": 9,
                "exp_year": 2023,
                "cvc": "123",
            })
        card_token = data['id']

        return card_token

    def create_payment_charge(self, card_token):
        payment = stripe.Charge.create(
            amount=self.amount,
            currency='usd',
            description=self.description,
            source=card_token,

        )

        payment_check = State.approved  # return True for successfull payment

        return payment_check