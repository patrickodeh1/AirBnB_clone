#!/usr/bin/python3
"""__init__.py"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


class_registry = {}


def register_class(cls):
    """Register a class in the class registry"""
    class_registry[cls.__name__] = cls

def get_class(name):
    """get a class from the class registry"""
    return class_registry.get(name)
