#!/usr/bin/python3
"""Module add_attribute"""


def add_attribute(obj, key, value):
    """ function that adds attributes"""
    
    try:
        setattr(obj, key, value)
    except AttributeError:
        raise TypeError("can't add new attribute")
