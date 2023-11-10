#!/usr/bin/python3
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class Test_FileStorage(unittest.TestCase):
    """This Class for test FileStorage"""

    def setUp(self):
        """method is called before every test method in the test class."""
        self.storage = FileStorage()

    def test_new_and_all(self):
        """Test the new and all methods"""
        obj = BaseModel()
        obj.save()
        Cls_id = f"{obj.__class__.__name__}.{obj.id}"

        """test key exist"""
        self.assertIn(Cls_id, self.storage.all())

        """Test obj exist"""
        self.assertEqual(self.storage.all()[Cls_id], obj)

    def test_save_and_reload(self):
        """Test the save and reload methods"""
        obj = BaseModel()
        obj.save()
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_key, new_storage.all())
        self.assertEqual(new_storage.all()[obj_key].id, obj.id)

    def test_save_and_reload_multiple_objects(self):
        """Test saving and reloading multiple objects"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        obj1_key = f"{obj1.__class__.__name__}.{obj1.id}"
        obj2_key = f"{obj2.__class__.__name__}.{obj2.id}"
        self.assertIn(obj1_key, new_storage.all())
        self.assertIn(obj2_key, new_storage.all())
        self.assertEqual(new_storage.all()[obj1_key].id, obj1.id)
        self.assertEqual(new_storage.all()[obj2_key].id, obj2.id)


if __name__ == '__main__':
    unittest.main()