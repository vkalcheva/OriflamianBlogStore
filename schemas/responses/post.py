from marshmallow import fields

from schemas.bases import PostBaseSchema


class PostResponseSchema(PostBaseSchema):
    id = fields.Integer(required=True)
    photo_url = fields.String(required=True)
    date_created = fields.DateTime(required=True)
    blogger_id = fields.Integer(required=True)