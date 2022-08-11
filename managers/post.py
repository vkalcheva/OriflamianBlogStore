from db import db
from models import PostModel


class PostManager:
    @staticmethod
    def create(data, user):
        data["blogger_id"] = user.id
        post = PostModel(**data)
        db.session.add(post)
        db.session.commit()
        return post