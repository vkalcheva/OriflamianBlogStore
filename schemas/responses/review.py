from marshmallow import fields

from schemas.bases import ReviewBaseSchema


class ReviewResponseSchema(ReviewBaseSchema):
    id = fields.Integer(required=True)
    post_date = fields.DateTime(required=True)
