#!/usr/bin/python3
"""base module"""


import csv
import json


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """from dict to json"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """from object to dict to file using json"""

        from models.rectangle import Rectangle
        from models.square import Square
        ls = list(cls.to_dictionary(i) for i in list_objs)
        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """from json to dict"""

        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create an instance"""

        dum = cls(1, 1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """load data from file"""

        try:
            with open('{}.json'.format(cls.__name__), 'r') as f:
                read = cls.from_json_string(f.read())
            return [cls.create(**i) for i in read]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to a csv file"""

        from models.rectangle import Rectangle
        from models.square import Square
        ls = list(cls.to_dictionary(i) for i in list_objs)
        with open('{}.csv'.format(cls.__name__), 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            for i in ls:
                if cls is Rectangle:
                    writer.writerow([i['id'], i['width'],
                                     i['height'], i['x'], i['y']])
                elif cls is Square:
                    writer.writerow([i['id'], i['size'], i['x'], i['y']])

    @classmethod
    def load_from_file_csv(cls):
        """ load from a csv file"""

        from models.rectangle import Rectangle
        from models.square import Square
        try:
            with open('{}.csv'.format(cls.__name__), 'r') as f:
                reader = csv.reader(f)
                keys_rect = ['id', 'width', 'height', 'x', 'y']
                keys_sq = ['id', 'size', 'x', 'y']
                dictionary = {}
                ls = []
                for row in reader:
                    for i, value in enumerate(row):
                        if cls is Rectangle:
                            dictionary[keys_rect[i]] = int(value)
                        elif cls is Square:
                            dictionary[keys_sq[i]] = int(value)
                    ls.append(dictionary)
                    dictionary = {}
            return [cls.create(**i) for i in ls]
        except FileNotFoundError:
            return []
