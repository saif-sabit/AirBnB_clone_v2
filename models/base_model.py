#!/usr/bin/python3
"""Base Model Module for HBNB project"""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage_type

Base = declarative_base()


class BaseModel:
    """Base class for all models in the HBNB project.

    Attributes:
        id (str): The unique identifier for the model.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """

    id = Column(String(60),
                nullable=False,
                primary_key=True,
                unique=True)
    created_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new model instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(v))
                elif k != '__class__':
                    setattr(self, k, v)
            if storage_type == 'db':
                if not hasattr(self, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                if not hasattr(self, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                if not hasattr(self, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Return a string representation of the instance."""
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute and save the instance to storage."""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert the instance into a dictionary format."""
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        for k, v in dct.items():
            if isinstance(v, datetime):
                dct[k] = v.isoformat()
        dct.pop('_sa_instance_state', None)
        return dct

    def delete(self):
        """Delete the current instance from storage."""
        from models import storage
        storage.delete(self)
