#!/usr/bin/python3
"""import models"""
from models.base_model import BaseModel
from unittest import TestCase
from datetime import datetime
import unittest


class Test_BaseModel_V1(TestCase):
    """this model test class basemodel"""

    def test_hasattr(self):
        # attribute exist
        att = BaseModel()
        self.assertTrue(hasattr(att, 'id'))
        self.assertTrue(hasattr(att, "created_at"))
        self.assertTrue(hasattr(att, "updated_at"))

    def test_id_if_it_uuid4(self):
        """test id"""
        a = BaseModel()
        # id == to uuid vesion 4
        compare = r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'
        self.assertRegex(str(a.id), compare)

    def test_method_to_dict(self):
        """test count key"""
        Td = BaseModel()
        key = Td.to_dict().keys()
        self.assertCountEqual(
            key, ['id', 'created_at', 'updated_at', '__class__'])

    def test_type(self):
        # test type
        a = BaseModel()
        dic = a.to_dict()
        # test type
        self.assertAlmostEqual(type(str(a)), str)
        self.assertAlmostEqual(type(a.id), str)
        self.assertAlmostEqual(type(a.created_at), datetime)
        self.assertAlmostEqual(type(a.updated_at), datetime)
        self.assertAlmostEqual(type(dic), dict)
        self.assertAlmostEqual(type(dic['id']), str)
        self.assertAlmostEqual(type(dic['created_at']), str)
        self.assertAlmostEqual(type(dic['updated_at']), str)
        self.assertAlmostEqual(type(dic['__class__']), str)

    def test_iso_format_Time(self):
        # test iso format.
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

    def test_unique_id(self):
        a = BaseModel()
        b = BaseModel()
        # test uniaue id
        self.assertNotEqual(a.id, b.id)

    def test_method_save(self):
        a = BaseModel()
        update_befor = a.updated_at
        a.save()
        update_after = a.updated_at
        # test updated time
        self.assertNotEqual(update_befor, update_after)

    def test_method_str(self):
        # test __str__:
        a = BaseModel()
        self.assertAlmostEqual(
            str(a), f"[{a.__class__.__name__}] ({a.id}) {a.__dict__}")

    def test_pass_argumemt(self):
        arg = BaseModel("test")
        with self.assertRaises(TypeError):
            arg.save("test")

        with self.assertRaises(TypeError):
            arg.to_dict("test")


if __name__ == '__main__':
    unittest.main()
