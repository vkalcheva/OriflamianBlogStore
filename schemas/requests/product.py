from marshmallow import Schema, fields


class ProductRequestSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=True)
    ingredients = fields.String(required=True)
    how_to_use = fields.String(required=True)
    image_url = fields.String(required=True)
    price = fields.Float(required=True)
    category_id = fields.Integer(required=True)
