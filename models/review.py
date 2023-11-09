#!/usr/bin/python3
"""import models"""

from models.base_model import BaseModel

"""model Review"""


class Review(BaseModel):
    """This file represent Class Review
        Public class attribute
            - place_id (str): is The place id of Review
            - user_id (str): it will be the user id
            - text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""
