#!/usr/bin/python3
"""import models"""
from models.user import User
from unittest import TestCase
from datetime import datetime
import unittest

"""model Test user"""


class Test_User(TestCase):
    """this model test class user"""

    def test_hasattr(self):
        """Test attr and methods"""
        new = User()
        new.name = "test"
        new.state_id = "test2"

        """Test attribute exist"""
        self.assertTrue(hasattr(new, 'id'))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "state_id"))

    def test_methods(self):
        """Test methods exist"""
        new = User()
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

    def test_type(self):
        """type test"""
        new = User()
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.name, str)
        self.assertIsInstance(new.state_id, str)


if __name__ == '__main__':
    unittest.main()
