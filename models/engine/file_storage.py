#!/usr/bin/python3
"""import models"""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new = FileStorage.__objects
        for CLS_id, obj in new.items():
            new[CLS_id] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(new, file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path)"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                dict_file = json.load(file)
                for cl_id, To_obj in dict_file.items():
                    FileStorage.__objects[cl_id] = BaseModel(**To_obj)
        except Exception:
            pass
