#!/usr/bin/python3
"""import models"""
from models.city import City
from unittest import TestCase
from datetime import datetime
import unittest

"""model Test city"""


class Test_City(TestCase):
    """this model test class City"""

    def test_hasattr(self):
        """Test attr and methods"""
        new = City()
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
        new = City()
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

    def test_type(self):
        """type test"""
        new = City()
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.name, str)
        self.assertIsInstance(new.state_id, str)


if __name__ == '__main__':
    unittest.main()
