import os.path
import uuid

from werkzeug.exceptions import NotFound

from constants import TEMP_DIR
from db import db
from models import ProductModel, CategoryType, CategoryModel
from services.s3 import S3Service
from utils.helpers import decode_file


class ProductManager:
    @staticmethod
    def get_all():
        # return ProductModel.query.filter_by(category_id=3).all()
        return ProductModel.query.order_by(ProductModel.category_id).all()

    # @staticmethod
    # def get_all():
    #     current_user = auth.current_user()
    #     if current_user.role == RoleType.complainer:
    #         return ComplaintModel.query.filter_by(complainer_id=current_user.id).all()
    #     elif current_user.role == RoleType.approver:
    #         return ComplaintModel.query.filter_by(status=State.pending).all()
    #     return ComplaintModel.query.all()

    @staticmethod
    def create(data, user):
        data["admin_id"] = user.id
        extension = data.pop("extension")
        image = data.pop("image")
        file_name = f"{str(uuid.uuid4())}.{extension}"
        path = os.path.join(TEMP_DIR, file_name)
        decode_file(path, image)
        s3 = S3Service()
        image_url = s3.upload_photo(path, file_name)
        try:
            data["image_url"] = image_url
            product = ProductModel(**data)
            db.session.add(product)
            db.session.flush()
            return product
        except Exception as ex:
            s3.delete_photo(file_name)
            raise ex
        finally:
            os.remove(path)

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

