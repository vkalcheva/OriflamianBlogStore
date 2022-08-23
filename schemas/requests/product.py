from marshmallow import fields

from schemas.bases import ProductBaseSchema


class ProductRequestSchema(ProductBaseSchema):
    image = fields.String(required=True, allow_none=True)
    extension = fields.String(required=True, allow_none=True)







