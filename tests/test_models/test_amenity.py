#!/usr/bin/python3
"""Unit tests for the Amenity class."""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity
import os

class TestAmenity(TestBaseModel):
    """Test cases for the Amenity class."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_type(self):
        """Test the type of the 'name' attribute."""
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.name), expected_type)

if __name__ == '__main__':
    unittest.main()
