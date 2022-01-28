from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, null
from sqlalchemy.orm import relationship

class Breed(Base):
    __tablename__ = 'breeds'
    id = Column(Integer, primary_key=True)
    breed_id = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User')