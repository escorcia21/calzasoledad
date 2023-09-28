from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from .BaseModel import EntityMeta

class CalzadoModel(EntityMeta):
    __tablename__ = 'calzado'

    id = Column(Integer, primary_key=True)
    nombre_producto = Column(String(255))
    tamaño = Column(String(255))
    color = Column(String(255))
    fecha_produccion = Column(DateTime)
    hora_produccion = Column(String(255))
    numero_paquete = Column(String(255))
    valor_produccion = Column(Float)

    def __init__(self, nombre_producto, tamaño, color, fecha_produccion, hora_produccion, numero_paquete, valor_produccion):
        self.nombre_producto = nombre_producto
        self.tamaño = tamaño
        self.color = color
        self.fecha_produccion = fecha_produccion
        self.hora_produccion = hora_produccion
        self.numero_paquete = numero_paquete
        self.valor_produccion = valor_produccion

    def __repr__(self):
        return {
            'id': self.id,
            'nombre_producto': self.nombre_producto,
            'tamaño': self.tamaño,
            'color': self.color,
            'fecha_produccion': self.fecha_produccion,
            'hora_produccion': self.hora_produccion,
            'numero_paquete': self.numero_paquete,
            'valor_produccion': self.valor_produccion
        }
