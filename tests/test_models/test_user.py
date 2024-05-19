#!/usr/bin/python3
"""defines the test for user.py"""

import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests cases for User"""

    def test_user_inherits_from_base_model(self):
        """
        Test if User class inherits from BaseModel.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        """
        Test if User attributes are correctly set and are strings.
        """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, "")

    def test_user_email(self):
        """
        Test setting and getting the email attribute.
        """
        user = User()
        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

    def test_user_password(self):
        """
        Test setting and getting the password attribute.
        """
        user = User()
        user.password = "password123"
        self.assertEqual(user.password, "password123")

    def test_user_first_name(self):
        """
        Test setting and getting the first_name attribute.
        """
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_user_last_name(self):
        """
        Test setting and getting the last_name attribute.
        """
        user = User()
        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
