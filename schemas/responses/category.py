from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import CategoryType


class CategoryResponseSchema(Schema):
    id = fields.Integer(required=True)
    type = EnumField(CategoryType)
