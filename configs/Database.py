from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv(override=True)

# Runtime Environment Configuration
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
DEBUG_MODE = os.environ.get('DEBUG_MODE').lower() == 'true'

# Create Database Engine
Engine = create_engine(
    SQLALCHEMY_DATABASE_URI, echo=DEBUG_MODE, future=True
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=Engine
)

Session = scoped_session(SessionLocal)