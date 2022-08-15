from db import db
from models.enums import CategoryType


class CategoryModel(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(CategoryType))

    admin_id = db.Column(db.Integer, db.ForeignKey("admins.id"), nullable=False)
    admin = db.relationship("AdminModel")