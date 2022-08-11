from marshmallow import Schema, fields


class PostRequestSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    photo_url = fields.String(required=True)
