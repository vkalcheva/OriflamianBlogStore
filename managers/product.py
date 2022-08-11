from werkzeug.exceptions import NotFound

from db import db
from models import ProductModel


class ProductManager:
    @staticmethod
    def get_all():
        return ProductModel.query.all()

    @staticmethod
    def create(data, user):
        data["admin_id"] = user.id
        product = ProductModel(**data)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update(product_data, id_):
        product_obj_query = ProductModel.query.filter_by(id=id_)
        product = product_obj_query.first()
        if not product:
            raise NotFound("This product does not exist")
        product_obj_query.update(product_data)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def delete(id_):
        product_obj_query = ProductModel.query.filter_by(id=id_)
        product = product_obj_query.first()
        if not product:
            raise NotFound("This product does not exist")
        db.session.delete(product)
        db.session.commit()

