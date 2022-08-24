import phonenumbers
from marshmallow import fields, validates, ValidationError, validate
from phonenumbers.phonenumberutil import NumberParseException

from schemas.requests.auth_base import AuthBase


class RegisterAdminRequestSchema(AuthBase):
    first_name = fields.String(required=True, validate=validate.Length(min=3))
    last_name = fields.String(required=True, validate=validate.Length(min=3))
    phone = fields.String(required=True)

    @validates("phone")
    def validate_phone(self, phone):
        try:
            phone_number = phonenumbers.parse(phone, None)
            phonenumbers.is_valid_number(phone_number)
        except NumberParseException:
            raise ValidationError("Not valid number!")


class LoginAdminRequestSchema(AuthBase):
    pass
