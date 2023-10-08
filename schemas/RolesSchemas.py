from marshmallow import Schema, fields

class CreateRoleSchema(Schema):
    userType = fields.Str(required=True)

class RoleByIdSchema(Schema):
    roleId = fields.Int(required=True)

class UpdateRoleSchema(Schema):
    roleId = fields.Int(required=True)
    userType = fields.Str(required=True)



