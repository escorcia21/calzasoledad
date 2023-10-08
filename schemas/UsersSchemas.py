from marshmallow import Schema, fields

class CreateUserSchema(Schema):
    cc = fields.Str(required=True)
    name = fields.Str(required=True)
    lastName = fields.Str(required=True)
    roleId = fields.Int(required=True)

class UserByIdSchema(Schema):
    cc = fields.Str(required=True)

class UpdateUserSchema(Schema):
    cc = fields.Str(required=True)
    name = fields.Str(required=True)
    lastName = fields.Str(required=True)
    roleId = fields.Int(required=True)
    
    