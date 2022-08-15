from marshmallow import fields

from schemas.bases import ProductBaseSchema


class ProductRequestSchema(ProductBaseSchema):
    description = fields.String(required=True)
    ingredients = fields.String(required=True)
    how_to_use = fields.String(required=True)

    image = fields.String(required=True)
    extension = fields.String(required=True)


