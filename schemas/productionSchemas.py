from marshmallow import Schema, fields

class CreateProductionSchema(Schema):
    employeeId = fields.Str(required=True)
    productId = fields.Int(required=True)
    productionDate = fields.Date(required=True)
    amount = fields.Int(required=True)

class ProductionByIdSchema(Schema):
    productionId = fields.Int(required=True)

class UpdateProductionSchema(Schema):
    productionId = fields.Int(required=True)
    productionDate = fields.Date(required=True)
    amount = fields.Int(required=True)