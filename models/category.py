from db import db


class CategoryModel(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)

    products = db.relationship("ProductModel", lazy="dynamic")

    admin_id = db.Column(db.Integer, db.ForeignKey("admins.id"), nullable=False)
    admin = db.relationship("AdminModel")