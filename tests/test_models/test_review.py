#!/usr/bin/python3
"""import models"""
from models.review import Review
from unittest import TestCase
from datetime import datetime
import unittest

"""model Test review"""


class Test_State(TestCase):
    """this model test class review"""

    def test_hasattr(self):
        """Test attr and methods"""
        new = Review()
        new.place_id = "test"
        new.user_id = "test2"
        new.text = "test3"

        """Test attribute exist"""
        self.assertTrue(hasattr(new, 'id'))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "place_id"))
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(hasattr(new, "text"))

    def test_methods(self):
        """Test methods exist"""
        new = Review()
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

    def test_type(self):
        """type test"""
        new = Review()
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.place_id, str)
        self.assertIsInstance(new.user_id, str)
        self.assertIsInstance(new.text, str)


if __name__ == '__main__':
    unittest.main()
