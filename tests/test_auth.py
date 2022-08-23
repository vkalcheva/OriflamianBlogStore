import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import BloggerModel


class TestAuth(TestCase):
    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_blogger(self):
        url = "/register"

        data = {
            "email": "new@mail.com",
            "password": "123$Qwer",
            "first_name": "Ivan",
            "last_name": "Ivanov",
            "phone": "+359893111111",
        }

        bloggers = BloggerModel.query.all()
        assert len(bloggers) == 0

        resp = self.client.post(url, json=data, headers={"Content-Type": "application/json"})

        assert resp.status_code == 201
        assert "token" in resp.json
        bloggers = BloggerModel.query.all()
        assert len(bloggers) == 1

    # def test_user_already_exists_raises(self):
    #     url = "/register"
    #     data = {
    #         "email": "ines@kenova3.com",
    #         "password": "123456",
    #         "first_name": "Ines",
    #         "last_name": "Kenova",
    #         "phone": "1234567890123",
    #         "iban": "BG80BNBG96611020345678",
    #     }
    #
    #     resp = self.client.post(
    #         url, data=json.dumps(data), headers={"Content-Type": "application/json"}
    #     )
    #
    #     assert resp.status_code == 201
    #
    #     # Make the same request but user already exists
    #
    #     resp = self.client.post(
    #         url, data=json.dumps(data), headers={"Content-Type": "application/json"}
    #     )
    #     assert resp.status_code == 400
    #     assert resp.json == {"message": "Please login"}


