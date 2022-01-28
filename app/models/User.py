import email
from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates, relationship
import bcrypt

# create a salt to hash passwords against
salt = bcrypt.gensalt()

# create a User class that inherits from the Base class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    
    @validates('email')
    def validate_email(self, key, email):
        #make sure email contains @ character
        assert '@' in email # if false, it will return an error
        return email
    
    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 4
        # encrypt password
        return bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def verify_password(self, password):
        # check the incoming password ('password' parameter) to the one saved on the User object ('self' parameter)
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8')
        )
    
    breed = relationship('Breed')