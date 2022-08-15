from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import CategoryType


class ProductBaseSchema(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)
    category_id = fields.Integer(required=True)


class CategoryBaseSchema(Schema):
    type = EnumField(CategoryType)


class PostBaseSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)


class ReviewBaseSchema(Schema):
    title = fields.String(required=True)
    comment = fields.String(required=True)
    post_id = fields.Integer(required=True)