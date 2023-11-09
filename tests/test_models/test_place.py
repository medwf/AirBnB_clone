#!/usr/bin/python3
"""import models"""
from models.place import Place
from unittest import TestCase
from datetime import datetime
import unittest

"""model Test Place"""


class test_Place(TestCase):
    """this model test class place"""

    def test_hasattr(self):
        """Test attr and methods"""
        new = Place()
        new.city_id = "test"
        new.user_id = "test2"
        new.name = "test3"
        new.description = "test3"
        new.number_bathrooms = 2
        new.number_rooms = 123
        new.max_guest = 12
        new.price_by_night = 10
        new.latitude = 3.2
        new.longitude = 2.3
        new.amenity_ids = ["a", "a"]

        """Test attribute exist"""
        self.assertTrue(hasattr(new, 'id'))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "city_id"))
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "description"))
        self.assertTrue(hasattr(new, "number_bathrooms"))
        self.assertTrue(hasattr(new, "number_rooms"))
        self.assertTrue(hasattr(new, "max_guest"))
        self.assertTrue(hasattr(new, "price_by_night"))
        self.assertTrue(hasattr(new, "latitude"))
        self.assertTrue(hasattr(new, "longitude"))
        self.assertTrue(hasattr(new, "amenity_ids"))

    def test_methods(self):
        """Test methods exist"""
        new = Place()
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

    def test_type(self):
        """type test"""
        new = Place()
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.city_id, str)
        self.assertIsInstance(new.user_id, str)
        self.assertIsInstance(new.name, str)
        self.assertIsInstance(new.description, str)
        self.assertIsInstance(new.number_bathrooms, int)
        self.assertIsInstance(new.number_rooms, int)
        self.assertIsInstance(new.max_guest, int)
        self.assertIsInstance(new.price_by_night, int)
        self.assertIsInstance(new.latitude, float)
        self.assertIsInstance(new.longitude, float)
        self.assertIsInstance(new.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
