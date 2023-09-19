#!/usr/bin/python3
"""Review module for the HBNB project"""

from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage_type

class Review(BaseModel, Base):
    """Review class to store review information"""

    # SQLAlchemy table name
    __tablename__ = 'reviews'

    # Define attributes based on storage_type
    if storage_type == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        # Default attributes for non-DB storage
        place_id = ""
        user_id = ""
        text = ""
