from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from models.BaseModel import Base

class Users(Base):
    __tablename__ = 'users'

    cc = mapped_column(String(255), primary_key=True)
    name = mapped_column(String(255), nullable=False)
    lastName = mapped_column(String(255), nullable=False)
    roleId = mapped_column(Integer, ForeignKey('roles.roleId'))
    password = mapped_column(String(255), nullable=False)

    role = relationship("Roles", back_populates="users", lazy='joined')

    def __init__(self, cc, name, lastName, roleId, password):
        self.cc = cc
        self.name = name
        self.lastName = lastName
        self.roleId = roleId
        self.password = password

    def __repr__(self):
        return {
            "cc": self.cc,
            "name": self.name,
            "lastName": self.lastName,
            "roleId": self.roleId,
            "role": self.role.__repr__()
        }