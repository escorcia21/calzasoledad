from marshmallow import Schema, fields

class CreateProductionSchema(Schema):
    employeeId = fields.Str(required=True)
    productId = fields.Int(required=True)
    productionDate = fields.Date(required=True)
    amount = fields.Int(required=True)

class ProductionByUserSchema(Schema):
    startProductionDate = fields.Date(required=True)
    endProductionDate = fields.Date(required=True)
    Authorization = fields.Str(required=True)


class UpdateProductionSchema(Schema):
    productionId = fields.Int(required=True)
    productionDate = fields.Date(required=True)
    amount = fields.Int(required=True)

class ProductionSchema(Schema): 
    productionDate = fields.Date(required=True)
    unitCompensation = fields.Float(required=True)
    packagesCompensation = fields.Float(required=True)
    productName = fields.Str(required=True)
    price = fields.Int(required=True)
    totalAmount = fields.Int(required=True)
    name = fields.Str(required=True)
    lastName = fields.Str(required=True)
    total_compensation = fields.Float(required=True)