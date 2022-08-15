from marshmallow import Schema, fields, validate, validates, ValidationError
from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    uppercase=1,  # need min. 1 uppercase letters
    numbers=1,  # need min. 1 digits
    special=1,  # need min. 1 special characters
    nonletters=1,  # need min. 1 non-letter characters (digits, specials, anything)
)


class AuthBase(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=20))

    @validates("password")
    def validate_password(self, value):
        errors = policy.test(value)
        if errors:
            raise ValidationError(f"Not a valid password")