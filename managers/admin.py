from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models import AdminModel


class AdminManager:
    @staticmethod
    def register(admin_data):
        admin_data["password"] = generate_password_hash(
            admin_data["password"], method="sha256"
        )
        admin = AdminModel(**admin_data)
        try:
            db.session.add(admin)
            db.session.commit()
            return AuthManager.encode_token(admin)
        except Exception as ex:
            raise BadRequest(str(ex))

    @staticmethod
    def login(data):
        try:
            admin = AdminModel.query.filter_by(email=data["email"]).first()
            if admin and check_password_hash(admin.password, data["password"]):
                return AuthManager.encode_token(admin)
            raise Exception
        except Exception:
            raise BadRequest("Invalid username or password")
