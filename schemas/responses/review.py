from marshmallow import Schema, fields


class ReviewResponseSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    comment = fields.String(required=True)
    post_date = fields.DateTime(required=True)
    post_id = fields.Integer(required=True)