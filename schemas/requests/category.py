from marshmallow import Schema
from marshmallow_enum import EnumField

from models import CategoryType


class CategoryRequestSchema(Schema):
    type = EnumField(CategoryType)