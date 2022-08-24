import os.path
import uuid

from constants import TEMP_DIR
from db import db
from models import ProductModel
from services.s3 import S3Service
from utils.helpers import decode_file


class ProductManager:
    @staticmethod
    def get_all():
        return ProductModel.query.order_by(ProductModel.category_id).all()

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
