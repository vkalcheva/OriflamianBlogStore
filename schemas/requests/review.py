from marshmallow import Schema, fields


class ReviewRequestSchema(Schema):
    title = fields.String(required=True)
    comment = fields.String(required=True)
    post_id = fields.Integer(required=True)