from sqlalchemy.orm import DeclarativeBase
from configs.Database import Engine

class Base(DeclarativeBase):
        pass

def init():
    Base.metadata.create_all(bind=Engine)