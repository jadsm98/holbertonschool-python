#!/usr/bin/python3
"""test case for rectangle class"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.rect1 = Rectangle(2, 4)
        self.rect2 = Rectangle(1, 1, 5, 0)
        self.rect3 = Rectangle(9, 8, 5, 1)
        self.rect4 = Rectangle(2, 3, 5, 2, 3)
        print(self.rect1.id)

    def tearDown(self):
        print('tearDown\n')

    def test_id(self):
        print('test_id')

        self.assertEqual(self.rect1.id + 1, self.rect2.id)
        self.assertEqual(self.rect4.id, 3)
        self.rect3.id = 6
        self.assertEqual(self.rect3.id, 6)

    def test_width(self):
        print('test_width')
        self.assertEqual(self.rect1.width, 2)
        self.assertEqual(self.rect2.width, 1)
        self.assertEqual(self.rect3.width, 9)
        self.assertEqual(self.rect4.width, 2)

        with self.assertRaises(TypeError):
            Rectangle('2', 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 3, 4, 2)
        with self.assertRaises(ValueError):
            Rectangle(-3, 1, 3)
        with self.assertRaises(TypeError):
            Rectangle(3.6, 1, 0, 0, 0)

        self.rect3.width = 6
        self.assertEqual(self.rect3.width, 6)
        with self.assertRaises(TypeError):
            self.rect1.width = [9, 7]
        with self.assertRaises(ValueError):
            self.rect2.width = -3
        with self.assertRaises(ValueError):
            self.rect4.width = 0

    def test_height(self):
        print('test_height')
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect2.height, 1)
        self.assertEqual(self.rect3.height, 8)
        self.assertEqual(self.rect4.height, 3)

        with self.assertRaises(TypeError):
            Rectangle(2, '5')
        with self.assertRaises(ValueError):
            Rectangle(3, 0, 4, 2)
        with self.assertRaises(ValueError):
            Rectangle(3, -1, 3)
        with self.assertRaises(TypeError):
            Rectangle(3, 1.4)

        self.rect3.height = 2
        self.assertEqual(self.rect3.height, 2)
        with self.assertRaises(TypeError):
            self.rect1.height = [9, 7]
        with self.assertRaises(ValueError):
            self.rect2.height = -3
        with self.assertRaises(ValueError):
            self.rect4.height = 0

    def test_x(self):
        print('test_x')
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect2.x, 5)

        with self.assertRaises(TypeError):
            Rectangle(2, 5, '4')
        with self.assertRaises(ValueError):
            Rectangle(3, 0, -4, 2)
        with self.assertRaises(TypeError):
            Rectangle(3, 1, 9.8, 8)

        self.rect3.x = 2
        self.assertEqual(self.rect3.x, 2)
        with self.assertRaises(TypeError):
            self.rect1.x = [9, 7]
        with self.assertRaises(ValueError):
            self.rect2.x = -3

    def test_y(self):
        print('test_y')
        self.assertEqual(self.rect1.y, 0)
        self.assertEqual(self.rect3.y, 1)

        with self.assertRaises(TypeError):
            Rectangle(2, 5, 7, '9')
        with self.assertRaises(ValueError):
            Rectangle(3, 1, 3, -7)
        with self.assertRaises(TypeError):
            Rectangle(3, 1, 6, 0.9)

        self.rect3.y = 2
        self.assertEqual(self.rect3.y, 2)
        with self.assertRaises(TypeError):
            self.rect1.y = [9, 7]
        with self.assertRaises(ValueError):
            self.rect2.y = -3

    def test_area(self):
        print('test_area')
        self.assertEqual(self.rect1.area(), 8)

    def test_display(self):
        print('test_display')
        self.dis1 = self.rect1.display()
        self.assertEqual(self.dis1, '##\n##\n##\n##')
        self.dis2 = self.rect4.display()
        self.assertEqual(self.dis2, '\n\n     ##\n     ##\n     ##')

    def test__str(self):
        self.assertEqual(self.rect4.__str__(), '[Rectangle] (3) 5/2 - 2/3')

    def test_update(self):
        self.rect1.update(3, 6, 1, 4)
        self.assertEqual(self.rect1.id, 3)
        self.assertEqual(self.rect1.width, 6)
        self.assertEqual(self.rect1.height, 1)
        self.assertEqual(self.rect1.x, 4)
        self.assertEqual(self.rect1.y, 0)

        with self.assertRaises(TypeError):
            self.rect2.update(2, '4')

        self.rect2.update(height=4, y=2)
        self.assertEqual(self.rect2.width, 1)
        self.assertEqual(self.rect2.height, 4)
        self.assertEqual(self.rect2.x, 5)
        self.assertEqual(self.rect2.y, 2)

        with self.assertRaises(ValueError):
            self.rect3.update(x=6, width=0, height=1)

    def test_dictionary(self):
        self.assertEqual(self.rect4.to_dictionary(),
                         {'id': 3, 'width': 2, 'height': 3, 'x': 5, 'y': 2})
