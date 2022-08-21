from marshmallow import Schema, fields


class ProductBaseSchema(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)
    category_id = fields.Integer(required=True)


class CategoryBaseSchema(Schema):
    type = fields.String(required=True)


class PostBaseSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)


class ReviewBaseSchema(Schema):
    title = fields.String(required=True)
    comment = fields.String(required=True)
    post_id = fields.Integer(required=True)