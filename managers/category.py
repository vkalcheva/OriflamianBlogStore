from db import db
from models import CategoryModel


class CategoryManager:
    @staticmethod
    def create(data, user):
        data["admin_id"] = user.id
        category = CategoryModel(**data)
        db.session.add(category)
        db.session.flush()
        return category
