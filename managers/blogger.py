from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models import BloggerModel


class BloggerManager:
    @staticmethod
    def register(blogger_data):
        blogger_data["password"] = generate_password_hash(
            blogger_data["password"], method="sha256"
        )
        blogger = BloggerModel(**blogger_data)
        try:
            db.session.add(blogger)
            db.session.flush()
            return AuthManager.encode_token(blogger)
        except Exception as ex:
            raise BadRequest(str(ex))

    @staticmethod
    def login(data):
        try:
            blogger = BloggerModel.query.filter_by(email=data["email"]).first()
            if blogger and check_password_hash(blogger.password, data["password"]):
                return AuthManager.encode_token(blogger)
            raise Exception
        except Exception:
            raise BadRequest("Invalid username or password")
