#!/usr/bin/python3
"""Unit tests for the Review class."""
import os
from tests.test_models.test_base_model import test_basemodel
from models.review import Review

class TestReview(test_basemodel):
    """Test class for the Review model."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test the 'place_id' attribute type."""
        new = self.value()
        self.assertEqual(type(new.place_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """Test the 'user_id' attribute type."""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_text(self):
        """Test the 'text' attribute type."""
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

if __name__ == '__main__':
    unittest.main()
