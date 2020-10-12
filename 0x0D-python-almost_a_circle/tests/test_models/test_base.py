#!/usr/bin/python3


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.base1 = Base()
        self.base2 = Base(6)
        self.base3 = Base()

    def test_base(self):
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 6)
        self.assertEqual(self.base3.id, 2)

