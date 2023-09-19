#!/usr/bin/python3
"""Unit tests for the Place class."""
import os
from tests.test_models.test_base_model import test_basemodel
from models.place import Place

class TestPlace(test_basemodel):
    """Test class for the Place model."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test the 'city_id' attribute type."""
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """Test the 'user_id' attribute type."""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """Test the 'name' attribute type."""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_description(self):
        """Test the 'description' attribute type."""
        new = self.value()
        self.assertEqual(type(new.description), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_rooms(self):
        """Test the 'number_rooms' attribute type."""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_bathrooms(self):
        """Test the 'number_bathrooms' attribute type."""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_max_guest(self):
        """Test the 'max_guest' attribute type."""
        new = this.value()
        self.assertEqual(type(new.max_guest), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_price_by_night(self):
        """Test the 'price_by_night' attribute type."""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_latitude(self):
        """Test the 'latitude' attribute type."""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_longitude(self):
        """Test the 'longitude' attribute type."""
        new = self.value()
        self.assertEqual(type(new.longitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_amenity_ids(self):
        """Test the 'amenity_ids' attribute type."""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

if __name__ == '__main__':
    unittest.main()
