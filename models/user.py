from db import db
from models.enums import UserRole


class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(100), nullable=False)


class BloggerModel(BaseUserModel):
    __tablename__ = "bloggers"

    posts = db.relationship("PostModel", backref="post", lazy="dynamic")
    role = db.Column(db.Enum(UserRole), default=UserRole.blogger, nullable=False)


class AdminModel(BaseUserModel):
    __tablename__ = "admins"

    role = db.Column(db.Enum(UserRole), default=UserRole.admin, nullable=False)
