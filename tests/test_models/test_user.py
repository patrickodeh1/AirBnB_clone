#!/usr/bin/python3
"""defines the test for user.py"""

import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Testcase for user"""
    def test_user_inherits_from_base_model(self):
        """tests if User class Inherits from basemodel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_uesr_attributes(self):
        """tests for user attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))


if __name__ == '__main__':
    unittest.main()
