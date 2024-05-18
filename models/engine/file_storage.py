#!/usr/bin/python3
"""file_storage.py"""


import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Handles the storage of all objects in a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        objects_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.exists(self.__file_path):
            return

        try:
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name = key.split('.')[0]
                    module = __import__('models.' + class_name.lower(), fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj_instance = cls(**value)
                    self.__objects[key] = obj_instance
        except Exception as e:
            pass

classes = {
    "BaseModel": BaseModel,
    "User": User
}

def reload_class(name):
    """deserializes ..."""
    return classes[name]

def reload(self):
    """deserializes ..."""
    try:
        with open(self.__file_path, "r") as file:
            obj_dict = json.load(file)
            for key, value in obj_dict.items():
                cls = reload_class(value["__class__"])
                self.__objects[key] = cls(**value)
    except FileNotFoundError:
        pass

    FileStorage.reload = reload
