from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship
from models.BaseModel import Base

class Roles(Base):
    __tablename__ = 'roles'

    roleId = mapped_column(Integer, primary_key=True)
    userType = mapped_column(String(255), nullable=False, unique=True)

    users = relationship("Users", back_populates="role")
    products = relationship("Products", back_populates="belongsTo")

    def __init__(self, userType):
        self.userType = userType

    def __repr__(self) -> str:
        return {
            "roleId": self.roleId,
            "userType": self.userType,
        }
