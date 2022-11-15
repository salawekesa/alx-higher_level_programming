#!/usr/bin/python3

"""This modules is the base module"""

class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_object=0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object +=1
            self.id = Base.__nb_object
