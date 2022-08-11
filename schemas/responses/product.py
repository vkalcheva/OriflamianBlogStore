from marshmallow import Schema, fields

from schemas.responses.category import CategoryResponseSchema


class ProductResponseSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)
    category = fields.Nested(CategoryResponseSchema)
