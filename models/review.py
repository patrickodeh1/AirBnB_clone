#!/usr/bin/python3
"""defines a class review"""
from models.base_model import BaseModel


class State(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
