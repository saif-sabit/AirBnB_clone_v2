#!/usr/bin/python3
"""User Module for HBNB project"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """User class for defining user attributes"""

    # SQLAlchemy table name
    __tablename__ = 'users'

    # Define attributes based on storage_type
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        # Default attributes for non-DB storage
        email = ""
        password = ""
        first_name = ""
        last_name = ""
