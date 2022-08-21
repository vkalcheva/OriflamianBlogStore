import datetime

from flask_testing import TestCase

from config import create_app
from db import db
from tests.factories import BloggerFactory
from tests.helpers import generate_token

ENDPOINTS_DATA = (
    ("/admin/products", "GET"),
    ("/admin/products", "POST"),
)


class TestApp(TestCase):
    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def iterate_endpoints(
        self,
        endpoints_data,
        status_code_method,
        expected_resp_body,
        headers=None,
        payload=None,
    ):
        if not headers:
            headers = {}
        if not payload:
            payload = {}

        resp = None
        for url, method in endpoints_data:
            if method == "GET":
                resp = self.client.get(url, headers=headers)
            elif method == "POST":
                resp = self.client.post(url, headers=headers)
            status_code_method(resp)
            self.assertEqual(resp.json, expected_resp_body)

    def test_login_required(self):
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Missing token"}
        )

    def test_invalid_token(self):
        headers = {"Authorization": "Bearer eyJ0eX"}
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Invalid token"}, headers
        )

    def test_expired_token(self):
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjYsImV4cCI6MTY2MDk5NTI0Niwicm9sZSI6IkJsb2dnZXJNb2RlbCJ9.9raKX1gbeSrMIOreR35tvt5lPOvwzSsgoGxYcf4AvX4"
        }
        payload = {
            "sub": 6,
            "exp": datetime.datetime(2022, 8, 20, 11, 34, 6, 478508),
            "role": "BloggerModel",
        }
        self.iterate_endpoints(
            ENDPOINTS_DATA,
            self.assert_401,
            {"message": "Token expired"},
            headers,
            payload,
        )

    def test_missing_permissions_for_admin(self):
        endpoints = (
            ("/admin/products", "GET"),
            ("/admin/products", "POST"),
        )
        user = BloggerFactory()
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        resp = None
        for url, method in endpoints:
            if method == "GET":
                resp = self.client.get(url, headers=headers)
            elif method == "POST":
                resp = self.client.post(url, headers=headers)
            self.assert403(resp)
            self.assertEqual(resp.json, {"message": "Permission denied!"})
