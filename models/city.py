#!/usr/bin/python3
"""City Module for HBNB project"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """City class for storing city information"""

    # SQLAlchemy table name
    __tablename__ = 'cities'

    # Define attributes based on storage_type
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        # Default attributes for non-DB storage
        name = ''
        state_id = ''
