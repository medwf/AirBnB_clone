#!/usr/bin/python3
"""import models"""
import json
from models.base_model import BaseModel
from models.user import User

"""model FileStorage"""


class FileStorage:
    """This file represent Class FileStorage
    privet instance Attribute:
        __file_path (str):  path to the JSON file (ex: file.json)
        __objects (dict): empty but will store all objects by <class name>.id

    Public instance Methodes:
        all: returns the dictionary __objects
        new: sets in __objects the obj with key <obj class name>.id
        save: serializes __objects to the JSON file (path: __file_path)
        reload:  deserializes the JSON file to __objects
                    (only if the JSON file (__file_path)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[k] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new = dict(FileStorage.__objects)
        for CLS_id, obj in new.items():
            new[CLS_id] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(new, file)

    def reload(self):
        """Deserializes the JSON file to __objects
            (only if the JSON file (__file_path)
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                dict_file = json.load(file)
                for cl_id, To_obj in dict_file.items():
                    if "BaseModel" in cl_id:
                        FileStorage.__objects[cl_id] = BaseModel(**To_obj)
                    elif "User" in cl_id:
                        FileStorage.__objects[cl_id] = User(**To_obj)
        except Exception:
            pass
