#!/usr/bin/python3
"""
    This module  returns the list of 
    available attributes and methods of 
    an object
"""

def lookup(obj):
    """
     returns the list of available attributes and methods of an object
    :param obj: defined
    :return:he list of available attributes and methods of an object
    """
    return (dir(obj))
