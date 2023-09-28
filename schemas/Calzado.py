from marshmallow import Schema, fields

class CalzadoSchema(Schema):
    nombre_producto = fields.Str(required=True)
    tamaño = fields.Int(required=True)
    color = fields.Str(required=True)
    numero_paquete = fields.Int(required=True)
    valor_produccion = fields.Float(required=True)

