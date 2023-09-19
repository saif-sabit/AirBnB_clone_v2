#!/usr/bin/python3
"""Unit tests for the City class."""
import os
from tests.test_models.test_base_model import test_basemodel
from models.city import City

class TestCity(test_basemodel):
    """Test class for the City model."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test the 'state_id' attribute type."""
        new = self.value()
        self.assertEqual(type(new.state_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """Test the 'name' attribute type."""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

if __name__ == '__main__':
    unittest.main()
