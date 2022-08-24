from db import db


class ProductModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    how_to_use = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    price = db.Column(db.Float(precision=2), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("CategoryModel")

    admin_id = db.Column(db.Integer, db.ForeignKey("admins.id"), nullable=False)
    admin = db.relationship("AdminModel")
