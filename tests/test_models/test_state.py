#!/usr/bin/python3
"""Unit tests for the State class."""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import os

class TestState(test_basemodel):
    """Test class for the State model."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """Test the 'name' attribute type."""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

if __name__ == '__main__':
    unittest.main()
