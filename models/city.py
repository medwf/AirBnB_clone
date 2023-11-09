#!/usr/bin/python3
"""import models"""

from models.base_model import BaseModel

"""model City"""


class City(BaseModel):
    """This file represent Class City
        Public class attribute
            - name (str): is The name of City
            - state_id (str): it will be the State.id
    """
    name = ""
    state_id = ""

