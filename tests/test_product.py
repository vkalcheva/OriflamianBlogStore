import os
from unittest.mock import patch

from flask_testing import TestCase

from config import create_app
from constants import TEMP_DIR
from db import db
from models import ProductModel
from services.s3 import S3Service
from tests.factories import AdminFactory
from tests.helpers import (
    generate_token,
    encoded_photo,
    encoded_photo_extension,
    mock_uuid,
)


class TestProduct(TestCase):
    url = "/admin/products"

    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_product_schema_missing_fields_raises(self):
        products = ProductModel.query.all()
        assert len(products) == 0

        user = AdminFactory()
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        data = {
            "price": 5,
            "description": "Test description",
            "ingredients": "Test ingredients",
            "how_to_use": "Test use",
            "image": encoded_photo,
            "extension": encoded_photo_extension,
        }

        resp = self.client.post(self.url, headers=headers, json=data)
        self.assert400(resp)

        assert resp.json == {'message': "Invalid fields {'name': ['Missing data for required field.']}"}

        products = ProductModel.query.all()
        assert len(products) == 0

    @patch("uuid.uuid4", mock_uuid)
    @patch.object(S3Service, "upload_photo", return_value="some.s3.url")
    def test_create_product(self, mocked_s3):
        products = ProductModel.query.all()
        assert len(products) == 0

        user = AdminFactory()
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        data = {
            "name": "Test name",
            "price": 5,
            "description": "Test description",
            "ingredients": "Test ingredients",
            "how_to_use": "Test use",
            "image": encoded_photo,
            "extension": encoded_photo_extension,
        }
        resp = self.client.post(self.url, headers=headers, json=data)
        assert resp.status_code == 201
        resp = resp.json
        expected_resp = {
            "name": data["name"],
            "image_url": mocked_s3.return_value,
            "category": None,
            "price": data["price"],
            "id": resp["id"],
            "category_id": None,
        }
        assert resp == expected_resp

        file_name = f"{str(mock_uuid())}.{encoded_photo_extension}"
        path = os.path.join(TEMP_DIR, file_name)

        mocked_s3.assert_called_once_with(path, file_name)

        products = ProductModel.query.all()
        assert len(products) == 1
