from marshmallow import fields

from schemas.bases import ProductBaseSchema


class ProductResponseSchema(ProductBaseSchema):
    id = fields.Integer(required=True)
    image_url = fields.String(required=True)

