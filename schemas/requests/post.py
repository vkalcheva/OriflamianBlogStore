from marshmallow import fields

from schemas.bases import PostBaseSchema


class PostRequestSchema(PostBaseSchema):
    photo = fields.String(required=True)
    photo_extension = fields.String(required=True)
