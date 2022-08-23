from marshmallow import fields

from schemas.bases import ProductBaseSchema
from schemas.responses.category import CategoryResponseSchema


class ProductResponseSchema(ProductBaseSchema):
    id = fields.Integer(required=True)
    image_url = fields.String(required=True, allow_none=True)
    category = fields.Nested(CategoryResponseSchema)




