#!/usr/bin/python3
"""
import uuid4 `uniquely identify version 4`
import datetime `give us time and date for update_at and create_at`
import storage Variable
"""
from uuid import uuid4
from datetime import datetime
import models
"""module BaseModel"""


class BaseModel:
    """This file represent Class BaseModel
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

    def __init__(self, *args, **kwargs):
        """Initialize a new Base object.
        Args:
            args (won't be used): list of argumments.
            kwargs: pass in dictionary as argumment.
        """
        if kwargs:
            for attr, v in kwargs.items():
                # fix error: type of created_at and updated_at most be datetime
                if attr in ('created_at', 'updated_at'):
                    Nv = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, attr, Nv)
                elif attr != "__class__":
                    setattr(self, attr, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return string represent name class and id and dict"""
        NameCls = "[{}] ".format(self.__class__.__name__)
        NameId = "({}) ".format(self.id)
        NameDict = "{}".format(self.__dict__)
        return NameCls + NameId + NameDict

    def save(self):
        """updates The updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary and change format datetime"""
        To_Dict = dict(self.__dict__)
        To_Dict['__class__'] = self.__class__.__name__
        # change format to %Y-%m-%dT%H:%M:%S.%f (ex:2017-06-14T22:31:03.285259)
        if type(To_Dict['created_at']) != str:
            To_Dict['created_at'] = To_Dict['created_at'].isoformat()
            To_Dict['updated_at'] = To_Dict['updated_at'].isoformat()
        return To_Dict
