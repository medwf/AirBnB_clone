#!/usr/bin/python3
"""
import baseModel
"""
from models.base_model import BaseModel
"""model User that inherits from BaseModel"""


class User(BaseModel):
    """This class represent User class attribute.

    Public class attribute:
        email (str): This attribute represent in email of User
        password (str): This attribute represent in password of User
        first_name (str): This attribute represent in first name  of User
        last_name (str): This attribute represent in last name of User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
