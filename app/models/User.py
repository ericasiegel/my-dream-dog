import email
from app.db import Base
from sqlalchemy import Column, Integer, String, null

# create a User class that inherits from the Base class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)