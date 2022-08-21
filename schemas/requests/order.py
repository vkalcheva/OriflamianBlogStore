from marshmallow import Schema, fields


class OrderSchemaRequest(Schema):
    products = fields.List(fields.Int())
