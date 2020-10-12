#!/usr/bin/python3

import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """tests square module"""

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.s1 = Square(3)
        self.s2 = Square(2, 3)
        self.s3 = Square(5, 1, 3)
        self.s4 = Square(4, 3, 2, 2)

    def tearDown(self):
        print('tearDown\n')

    def test_init(self):
        self.assertIsInstance(self.s1, Square)
        self.assertIsInstance(self.s1, Rectangle)
        self.assertIsInstance(self.s3, Rectangle)

        self.assertEqual(self.s3.size, 5)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.x, 3)

        self.assertEqual(self.s1.id + 1, self.s2.id)
        with self.assertRaises(TypeError):
            Square('5')
        with self.assertRaises(ValueError):
            Square(-3, 2, 3)
        with self.assertRaises(TypeError):
            Square(3, True, 1)
        with self.assertRaises(ValueError):
            Square(2, 5, -1)
        with self.assertRaises(TypeError):
            Square()

        self.s1.size = 5
        self.s1.x = 2
        self.s1.y = 1
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.x, 2)
        self.assertEqual(self.s1.y, 1)

        with self.assertRaises(TypeError):
            self.s1.size = '5'
        with self.assertRaises(ValueError):
            self.s1.size = -5
        with self.assertRaises(ValueError):
            self.s1.x = -2
        with self.assertRaises(TypeError):
            self.s1.y = True

        self.assertTrue(self.s2.size == self.s2.height)
        self.assertTrue(self.s2.size == self.s2.width)

    def test_str(self):
        self.assertEqual(self.s4.__str__(), '[Square] (2) 3/2 - 4')

    def test_area(self):
        self.assertEqual(self.s1.area(), 9)

    def test_display(self):

        self.dis1 = self.s1.display()
        self.assertEqual(self.dis1, '###\n###\n###')
        self.dis2 = self.s2.display()
        self.assertEqual(self.dis2, '   ##\n   ##')

    def test_update(self):

        self.s1.update(3, 6, 1, 4)
        self.assertEqual(self.s1.id, 3)
        self.assertEqual(self.s1.size, 6)
        self.assertEqual(self.s1.x, 1)
        self.assertEqual(self.s1.y, 4)

        with self.assertRaises(TypeError):
            self.s1.update(2, '4')

        self.s2.update(size=4, y=2, id=3)
        self.assertEqual(self.s2.size, 4)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s2.y, 2)
        self.assertEqual(self.s2.id, 3)

        with self.assertRaises(ValueError):
            self.s3.update(x=6, size=0, id=1)

    def test_dictionary(self):
        self.assertEqual(self.s4.to_dictionary(),
                         {'id': 2, 'size': 4, 'x': 3, 'y': 2})
