#!/usr/bin/python3
"""defines the test for user.py"""


import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    """Testcase for user"""
    def setUp(self):
        """reloads storage before each test"""
        self.storage = FileStorage()
        self.storage.reload()
        self.storage.all().clear()

    def tearDown(self):
        """saves storage after each test"""
        self.storage.save()
        self.storage.all().clear()

    def test_attributes(self):
        """test if attributes are initiaalied correctly"""
        user = User()

        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertEqual(user.created_at, user.updated_at)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_save_method(self):
        """Test the save method"""
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        user = User()
        obj_dict = user.to_dict()

        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], user.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], user.updated_at.isoformat())

    def test_str_method(self):
        """Test the __str__ method"""
        user = User()

        expected_str = "[BaseModel] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_init_method_with_kwargs(self):
        """ Test __init__ method with kwargs"""
        data = {
            'id': '123',
            'created_at': '2024-05-14T12:30:00.000000',
            'updated_at': '2024-05-14T12:30:00.000000',
            'email': 'myemail@example.com',
            'password': 'password',
            'first_name': 'Test',
            'last_name': 'User'

        }
        user = User(**data)

        self.assertEqual(user.id, '123')
        self.assertEqual(user.created_at, datetime.fromisoformat(data['created_at']))
        self.assertEqual(user.updated_at, datetime.fromisoformat(data['updated_at']))
        self.assertEqual(user.email, 'myemail@example.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')

    def test_new_method(self):
        """test the new method of FileStorage"""
        user = User()
        key = 'User.' + user.id
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()
