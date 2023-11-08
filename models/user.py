#!/usr/bin/python3
"""
import baseModel
"""
from models.base_model import BaseModel
"""model User that inherits from BaseModel"""


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
