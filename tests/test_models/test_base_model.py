#!/usr/bin/python3
"""import models"""
from models.base_model import BaseModel
from unittest import TestCase

"""model test basemodel"""


class Test_BaseModel(TestCase):
    """this model test class basemodel"""

    def test_id_instance(self):
        """test id using Regex"""
        a = BaseModel()
        compare = r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'
        self.assertRegex(str(a.id), compare)
        self.assertRegex(str(a.created_at), r"[]")
