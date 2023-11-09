#!/usr/bin/python3
"""import models"""
from models.state import State
from unittest import TestCase
from datetime import datetime
import unittest

"""model Test State"""


class Test_State(TestCase):
    """this model test class basemodel"""

    def test_hasattr(self):
        """Test attr and methods"""
        new = State()
        new.name = "test"

        """Test attribute exist"""
        self.assertTrue(hasattr(new, 'id'))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))

    def test_methods(self):
        """Test methods exist"""
        new = State()
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

    def test_type(self):
        """type test"""
        new = State()
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.name, str)


if __name__ == '__main__':
    unittest.main()
