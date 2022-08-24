from marshmallow import fields

from schemas.bases import CategoryBaseSchema


class CategoryResponseSchema(CategoryBaseSchema):
    id = fields.Integer(required=True)
