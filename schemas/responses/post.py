from marshmallow import Schema, fields


class PostResponseSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    photo_url = fields.String(required=True)
    date_created = fields.DateTime(required=True)
    blogger_id = fields.Integer(required=True)