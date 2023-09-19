#!/usr/bin/python3
"""Unit tests for the HBNBCommand class (console command interpreter)."""
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from tests import clear_stream

class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""
    
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """Test the create command with FileStorage."""
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            
            # Create a City instance
            cons.onecmd('create City name="Texas"')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            self.assertIn('City.{}'.format(mdl_id), storage.all().keys())
            
            # Check the attributes of the created City instance
            cons.onecmd('show City {}'.format(mdl_id))
            self.assertIn("'name': 'Texas'", cout.getvalue().strip())
            clear_stream(cout)
            
            # Create a User instance
            cons.onecmd('create User name="James" age=17 height=5.9')
            mdl_id = cout.getvalue().strip()
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())
            clear_stream(cout)
            
            # Check the attributes of the created User instance
            cons.onecmd('show User {}'.format(mdl_id))
            self.assertIn("'name': 'James'", cout.getvalue().strip())
            self.assertIn("'age': 17", cout.getvalue().strip())
            self.assertIn("'height': 5.9", cout.getvalue().strip())

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_create(self):
        """Test the create command with DBStorage."""
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            
            # Attempt to create a User instance with missing attributes
            with self.assertRaises(sqlalchemy.exc.OperationalError):
                cons.onecmd('create User')
            
            # Create a User instance with specified attributes
            clear_stream(cout)
            cons.onecmd('create User email="john25@gmail.com" password="123"')
            mdl_id = cout.getvalue().strip()
            
            # Connect to the database and verify the User instance
            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(mdl_id))
            result = cursor.fetchone()
            self.assertTrue(result is not None)
            self.assertIn('john25@gmail.com', result)
            self.assertIn('123', result)
            cursor.close()
            dbc.close()

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_show(self):
        """Test the show command with DBStorage."""
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            
            # Create a User instance and verify it does not exist in the DB
            obj = User(email="john25@gmail.com", password="123")
            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(obj.id))
            result = cursor.fetchone()
            self.assertTrue(result is None)
            
            # Use the 'show' command to find the non-existent User instance
            cons.onecmd('show User {}'.format(obj.id))
            self.assertEqual(
                cout.getvalue().strip(),
                '** no instance found **'
            )
            
            # Save the User instance and verify it exists in the DB
            obj.save()
            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(obj.id))
            
            # Use the 'show' command to find the User instance
            clear_stream(cout)
            cons.onecmd('show User {}'.format(obj.id))
            result = cursor.fetchone()
            self.assertTrue(result is not None)
            self.assertIn('john25@gmail.com', result)
            self.assertIn('123', result)
            self.assertIn('john25@gmail.com', cout.getvalue())
            self.assertIn('123', cout.getvalue())
            cursor.close()
            dbc.close()

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_count(self):
        """Test the count command with DBStorage."""
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            
            # Connect to the DB and get the initial count of states
            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT COUNT(*) FROM states;')
            res = cursor.fetchone()
            prev_count = int(res[0])
            
            # Create a new State instance
            cons.onecmd('create State name="Enugu"')
            clear_stream(cout)
            
            # Use the 'count' command to count the number of State instances
            cons.onecmd('count State')
            cnt = cout.getvalue().strip()
            self.assertEqual(int(cnt), prev_count + 1)
            
            # Verify the count again
            clear_stream(cout)
            cons.onecmd('count State')
            cursor.close()
            dbc.close()

if __name__ == '__main__':
    unittest.main()
