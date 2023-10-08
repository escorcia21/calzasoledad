from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from models.BaseModel import Base

class Products(Base):
    __tablename__ = 'products'

    productId = mapped_column(Integer, primary_key=True)
    productName = mapped_column(String(255), nullable=False, unique=True)
    price = mapped_column(Float, nullable=False)
    unitCompensation = mapped_column(Float, nullable=False)
    packagesCompensation = mapped_column(Float, nullable=False)
    productRoleId = mapped_column(Integer, ForeignKey('roles.roleId'), nullable=False)

    belongsTo = relationship("Roles", back_populates="products")

    def __init__(self, productName, price, unitCompensation, packagesCompensation, productRoleId):
        self.productName = productName
        self.price = price
        self.unitCompensation = unitCompensation
        self.packagesCompensation = packagesCompensation
        self.productRoleId = productRoleId

    def __repr__(self):
        return {
            'productId': self.productId,
            'productName': self.productName,
            'price': self.price,
            'unitCompensation': self.unitCompensation,
            'packagesCompensation': self.packagesCompensation,
            'productRoleId': self.productRoleId,
            'productRole': self.belongsTo.__repr__()
        }