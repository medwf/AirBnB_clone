#!/usr/bin/python3
"""
import uuid4 `uniquely identify version 4`
import datetime `give us time and date for update_at and create_at`
"""
from uuid import uuid4
from datetime import datetime
"""module BaseModel"""


class BaseModel:
    """This file represent Class Basemode
    Public instance Attribute:
        id (str): create unique id for new object.
        created_at (datetime): The current datetime when an instance is created
        update_at (datetime): The current datetime when an instance is created
                                    and it will be updated

    Public instance Methodes:
        __str__: return string represent name class and id and dict
        save: updates The updated_at with the current datetime
        to_dict: returns a dictionary, change format datetime
    """

    def __init__(self):
        """Initialize a new Base object.
        Args:
            no args
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return string represent name class and id and dict"""
        NameCls = "[{}] ".format(self.__class__.__name__)
        NameId = "({}) ".format(self.id)
        NameDict = "{}".format(self.__dict__)
        return NameCls + NameId + NameDict

    def save(self):
        """updates The updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary and change format datetime"""
        To_Dict = dict(self.__dict__)
        To_Dict['__class__'] = self.__class__.__name__
        # change format to %Y-%m-%dT%H:%M:%S.%f (ex:2017-06-14T22:31:03.285259)
        To_Dict['created_at'] = To_Dict['created_at'].isoformat()
        To_Dict['updated_at'] = To_Dict['updated_at'].isoformat()
        return To_Dict
