from sqlalchemy import func

from db import db
from models.enums import State

products_orders = db.Table(
    "products_orders",
    db.Model.metadata,
    db.Column("product_id", db.Integer, db.ForeignKey("products.id")),
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id")),
)


class OrderModel(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    status = db.Column(db.Enum(State), default=State.pending, nullable=False)

    products = db.relationship("ProductModel", secondary=products_orders)