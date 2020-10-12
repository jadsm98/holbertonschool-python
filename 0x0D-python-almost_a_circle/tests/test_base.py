#!/usr/bin/python3
"""test cases for base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self):
        print('setUp')

        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(7)

    def test_init(self):
        print('test_init')

        self.assertEqual(self.b1.id + 1, self.b2.id)
        self.assertEqual(self.b3.id, 7)

    def test_to_json_string(self):
        print('test_to_json_string')

        self.dct1 = {'hey': 3, 'you': True, 4: (3, 9)}
        self.dct2 = {3: 5, 'y': 'i'}
        self.assertEqual(Base.to_json_string([self.dct1, self.dct2]),
                         '[{"hey": 3, "you": true, "4": [3, 9]}, {"3": 5, "y": "i"}]')
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        print('test_save_to_file')
        self.r1 = Square(1, 2, 6, 2)
        self.r2 = Square(2, 5, 7, 1)
        Rectangle.save_to_file([self.r1, self.r2])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            print(read)
        self.assertMultiLineEqual(read, '[{"id": 2, "size": 1, "x": 2, "y": 6}, {"id": 1, "size": 2, "x": 5, "y": 7}]')

    def test_from_json_string(self):
        print('test_from_json_string')
        self.list_input1 = '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'
        self.list_input2 = ''
        self.list_input3 = None
        self.assertEqual(Rectangle.from_json_string(self.list_input1),
                         [{'height': 4, 'width': 10, 'id': 89},
                          {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(Rectangle.from_json_string(self.list_input2), [])
        self.assertEqual(Rectangle.from_json_string(self.list_input3), [])

    def test_create(self):
        print('test_create')
        self.r3 = Rectangle.create(**{'height': 4, 'width': 10, 'id': 89})
        self.assertIsInstance(self.r3, Rectangle)
        self.assertEqual(self.r3.__str__(), '[Rectangle] (89) 0/0 - 10/4')

    def test_load_from_file(self):
        print('test_load_from_file')
        self.r1 = Rectangle(10, 7, 2, 8, 10)
        self.r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangles_input = [self.r1, self.r2]
        Rectangle.save_to_file(list_rectangles_input)
        self.list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(self.list_rectangles_output[0].__str__(),
                         '[Rectangle] (10) 2/8 - 10/7')
        self.assertEqual(self.list_rectangles_output[1].__str__(),
                         '[Rectangle] (2) 0/0 - 2/4')


