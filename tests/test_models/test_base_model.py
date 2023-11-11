#!/usr/bin/python3
"""import models"""
from models.base_model import BaseModel
from unittest import TestCase
from datetime import datetime
from unittest.mock import patch
import unittest
import json
import os


class Test_BaseModel_V1(TestCase):
    """this model test class basemodel"""

    def test_hasattr(self):
        """Test attr and methods"""
        att = BaseModel()

        """Test attribute exist"""
        self.assertTrue(hasattr(att, 'id'))
        self.assertTrue(hasattr(att, "created_at"))
        self.assertTrue(hasattr(att, "updated_at"))

        att.name = "test"
        att.age = 11
        self.assertTrue(hasattr(att, "name"))
        self.assertTrue(hasattr(att, "age"))

        """Test methods exist"""
        self.assertTrue(hasattr(att, "__init__"))
        self.assertTrue(hasattr(att, "__str__"))
        self.assertTrue(hasattr(att, "save"))
        self.assertTrue(hasattr(att, "to_dict"))

    def test_to_dict(self):
        """test count key"""
        Td = BaseModel()
        key = Td.to_dict().keys()
        self.assertCountEqual(
            key, ['id', 'created_at', 'updated_at', '__class__'])

    def test_type(self):
        """test type"""
        a = BaseModel()
        dic = a.to_dict()

        self.assertAlmostEqual(type(str(a)), str)
        self.assertAlmostEqual(type(a.id), str)
        self.assertAlmostEqual(type(a.created_at), datetime)
        self.assertAlmostEqual(type(a.updated_at), datetime)
        self.assertAlmostEqual(type(dic), dict)
        self.assertAlmostEqual(type(dic['id']), str)
        self.assertAlmostEqual(type(dic['created_at']), str)
        self.assertAlmostEqual(type(dic['updated_at']), str)
        self.assertAlmostEqual(type(dic['__class__']), str)

    def test_Time(self):
        """test iso format."""
        a = BaseModel()
        time = a.to_dict()['created_at']
        cr = datetime.strptime(
            time, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(time, cr.strftime(
            "%Y-%m-%dT%H:%M:%S.%f"))

        time = a.to_dict()['updated_at']
        cr = datetime.strptime(
            time, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(time, cr.strftime(
            "%Y-%m-%dT%H:%M:%S.%f"))

    def test_unique(self):
        """test unique"""
        a = BaseModel()
        b = BaseModel()
        # test uniaue id
        self.assertNotEqual(a.id, b.id)
        """unique obj"""
        self.assertNotEqual(a, b)

    def test_save(self):
        a = BaseModel()
        update_befor = a.updated_at
        a.save()
        update_after = a.updated_at
        # test updated time
        self.assertNotEqual(update_befor, update_after)

    def test_str(self):
        """test __str__"""
        a = BaseModel()
        self.assertAlmostEqual(
            str(a), f"[{a.__class__.__name__}] ({a.id}) {a.__dict__}")

    def test_pass_argumemt(self):
        """test pass rong argumment"""
        arg = BaseModel("test")
        with self.assertRaises(TypeError):
            arg.save("test")

        with self.assertRaises(TypeError):
            arg.to_dict("test")


class Test_BaseModel_V2(TestCase):
    """this model test class basemodel"""

    def test_args(self):
        """test pass args no change"""
        a = BaseModel(None)
        dic = a.to_dict()
        b = BaseModel("None", 12)

        """test object"""
        self.assertNotEqual(a, b)

        """Test unique id"""
        self.assertNotEqual(a.id, b.id)

        """test Type Time"""
        self.assertAlmostEqual(type(b.created_at), datetime)
        self.assertAlmostEqual(type(b.updated_at), datetime)

    def test_kwargs(self):
        """test pass Kwargs"""
        x = BaseModel()
        x.name = "test"
        x.my_number = 11
        kv = x.to_dict()
        y = BaseModel(**kv)
        self.assertEqual(x.id, y.id)
        self.assertEqual(x.name, "test")
        self.assertEqual(x.my_number, 11)
        self.assertEqual(x.to_dict(), y.to_dict())

    def test_saveV2(self):
        """test save() Calling storage.save()"""
        """ check if init it call: models.storage.save() """
        with patch('models.storage.save') as mk:
            oj = BaseModel()
            oj.save()
            mk.assert_called_once()

    def test_json_file(self):
        """test if it save in json file"""
        """clear all """
        os.remove("file.json")

        """start testing"""
        oj = BaseModel()
        ky = f"BaseModel.{oj.id}"
        oj.save()
        with open("file.json", 'r') as file:
            dic = json.load(file)
        """ check if ky in dic"""
        self.assertIn(ky, dic)


if __name__ == '__main__':
    unittest.main()
