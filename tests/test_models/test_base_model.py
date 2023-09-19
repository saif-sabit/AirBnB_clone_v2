#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import os
import unittest
import json
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'BaseModel test not supported for database storage')
class TestBaseModel(unittest.TestCase):
    """Test class for the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class for BaseModel."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up method for the test class."""
        pass

    def tearDown(self):
        """Teardown method for the test class."""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init(self):
        """Test the initialization of the BaseModel class."""
        self.assertIsInstance(self.value(), BaseModel)
        if self.value is not BaseModel:
            self.assertIsInstance(self.value(), Base)
        else:
            self.assertNotIsInstance(self.value(), Base)

    def test_default(self):
        """Test the default values of BaseModel."""
        instance = self.value()
        self.assertEqual(type(instance), self.value)

    def test_kwargs(self):
        """Test BaseModel with kwargs."""
        instance = self.value()
        copy = instance.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is instance)

    def test_kwargs_int(self):
        """Test BaseModel with integer kwargs."""
        instance = self.value()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test the save method of BaseModel."""
        instance = self.value()
        instance.save()
        key = self.name + "." + instance.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], instance.to_dict())

    def test_str(self):
        """Test the __str__ method of BaseModel."""
        instance = self.value()
        self.assertEqual(str(instance), '[{}] ({}) {}'.format(
            self.name, instance.id, instance.__dict__))

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        instance = self.value()
        n = instance.to_dict()
        self.assertEqual(instance.to_dict(), n)
        self.assertIsInstance(self.value().to_dict(), dict)
        self.assertIn('id', self.value().to_dict())
        self.assertIn('created_at', self.value().to_dict())
        self.assertIn('updated_at', self.value().to_dict())
        mdl = self.value()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', self.value(firstname='Celestine').to_dict())
        self.assertIn('lastname', self.value(lastname='Akpanoko').to_dict())
        self.assertIsInstance(self.value().to_dict()['created_at'], str)
        self.assertIsInstance(self.value().to_dict()['updated_at'], str)
        datetime_now = datetime.today()
        mdl = self.value()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': mdl.__class__.__name__,
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertDictEqual(
                self.value(id='u-b34', age=13).to_dict(),
                {
                    '__class__': mdl.__class__.__name__,
                    'id': 'u-b34',
                    'age': 13
                }
            )
            self.assertDictEqual(
                self.value(id='u-b34', age=None).to_dict(),
                {
                    '__class__': mdl.__class__.__name__,
                    'id': 'u-b34',
                    'age': None
                }
            )
        mdl_d = self.value()
        self.assertIn('__class__', self.value().to_dict())
        self.assertNotIn('__class__', self.value().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )

    def test_kwargs_none(self):
        """Test BaseModel with kwargs containing None."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test BaseModel with kwargs containing one argument."""
        n = {'name': 'test'}
        new = self.value(**n)
        self.assertEqual(new.name, n['name'])

    def test_id(self):
        """Test the 'id' attribute of the model."""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test the 'created_at' attribute of the model."""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """Test the 'updated_at' attribute of the model."""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == '__main__':
    unittest.main()
