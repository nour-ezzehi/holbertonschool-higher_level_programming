#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.square = Square(size=5, x=2, y=3, id=1)

    def test_constructor(self):
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_getters(self):
        self.assertEqual(self.square.size, 5)

    def test_setters(self):
        self.square.size = 7
        self.assertEqual(self.square.size, 7)
        self.assertEqual(self.square.width, 7)
        self.assertEqual(self.square.height, 7)

        self.square.x = 3
        self.assertEqual(self.square.x, 3)
        self.square.y = 4
        self.assertEqual(self.square.y, 4)

    def test_str(self):
        self.assertEqual(str(self.square), "[Square] (1) 2/3 - 5")

    def test_update(self):
        self.square.update(2, 3, 4, 5)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 3)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 5)

        self.square.update(size=6, x=7, y=8, id=9)
        self.assertEqual(self.square.id, 9)
        self.assertEqual(self.square.size, 6)
        self.assertEqual(self.square.x, 7)
        self.assertEqual(self.square.y, 8)

    def test_to_dictionary(self):
        dictionary_representation = {
            'id': 1,
            'x': 2,
            'size': 5,
            'y': 3
        }
        self.assertEqual(self.square.to_dictionary(), dictionary_representation)

if __name__ == '__main__':
    unittest.main()
