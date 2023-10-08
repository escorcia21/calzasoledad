from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from models.BaseModel import Base

class Production(Base):
    __tablename__ = 'production'

    productionId = mapped_column(Integer, primary_key=True, nullable=False)
    employeeId = mapped_column(String(255), ForeignKey('users.cc'), nullable=False)
    productId = mapped_column(Integer, ForeignKey('products.productId'), nullable=False)
    productionDate = mapped_column(Date, nullable=False)
    amount = mapped_column(Integer, nullable=False)

    def __init__(self, employeeId, productId, productionDate, amount):
        self.employeeId = employeeId
        self.productId = productId
        self.productionDate = productionDate
        self.amount = amount

    def __repr__(self):
        return {
            "productionId": self.productionId,
            "employeeId": self.employeeId,
            "productId": self.productId,
            "productionDate": self.productionDate,
            "amount": self.amount
        }