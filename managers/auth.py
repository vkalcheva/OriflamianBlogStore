from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import BadRequest, Unauthorized

from models import AdminModel, BloggerModel

mapper = {
    "AdminModel": lambda x: AdminModel.query.filter_by(id=x).first(),
    "BloggerModel": lambda x: BloggerModel.query.filter_by(id=x).first(),
}


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(days=100),
            "role": user.__class__.__name__,
        }
        return jwt.encode(payload, key=config("SECRET_KEY"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        if not token:
            raise Unauthorized("Missing token")
        try:
            data = jwt.decode(
                jwt=token, key=config("SECRET_KEY"), algorithms=["HS256"]
            )
            return data["sub"], data["role"]
        except ExpiredSignatureError:
            raise Unauthorized("Token expired")
        except InvalidTokenError:
            raise Unauthorized("Invalid token")


auth = HTTPTokenAuth()


@auth.verify_token
def verify_token(token):
    user_id, role = AuthManager.decode_token(token)
    user = mapper[role](user_id)
    return user
