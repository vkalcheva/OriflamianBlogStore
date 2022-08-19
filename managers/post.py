import os
import uuid

from constants import TEMP_DIR
from db import db
from models import PostModel
from services.s3 import S3Service
from utils.helpers import decode_file


class PostManager:
    @staticmethod
    def create(data, user):
        data["blogger_id"] = user.id
        photo_extension = data.pop("photo_extension")
        photo = data.pop("photo")
        file_name = f"{str(uuid.uuid4())}.{photo_extension}"
        path = os.path.join(TEMP_DIR, file_name)
        decode_file(path, photo)
        s3 = S3Service()
        photo_url = s3.upload_photo(path, file_name)
        try:
            data["photo_url"] = photo_url
            post = PostModel(**data)
            db.session.add(post)
            db.session.flush()
            return post
        except Exception as ex:
            s3.delete_photo(file_name)
            raise ex
        finally:
            os.remove(path)