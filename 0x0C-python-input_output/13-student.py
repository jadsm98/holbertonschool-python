#!/usr/bin/python3
"""module"""


class Student:
    """class Students"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(i) is str for i in attrs):
            dic = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    dic[key] = value
            return dic
        return self.__dict__
        
    def reload_from_json(self, json):
        self.__dict__ = json
        return self.__dict__
