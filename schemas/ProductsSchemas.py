from marshmallow import Schema, fields

class CreateProductSchema(Schema):
    productName = fields.Str(required=True)
    price = fields.Float(required=True)
    unitCompensation = fields.Float(required=True)
    packagesCompensation = fields.Float(required=True)
    productRoleId = fields.Int(required=True)

class UpdateProductSchema(Schema):
    productId = fields.Int(required=True)
    productName = fields.Str(required=True)
    price = fields.Float(required=True)
    unitCompensation = fields.Float(required=True)
    packagesCompensation = fields.Float(required=True)
    productRoleId = fields.Int(required=True)

