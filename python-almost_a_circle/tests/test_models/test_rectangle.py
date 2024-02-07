#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):

    def setUp(self):

        self.rectangle = Rectangle(width=5, height=10, x=2, y=3, id=1)

    def test_constructor(self):
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 10)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 3)
        self.assertEqual(self.rectangle.id, 1)

    def test_setters(self):
        self.rectangle.x = 7
        self.assertEqual(self.rectangle.x, 7)
        self.rectangle.y = 8
        self.assertEqual(self.rectangle.y, 8)
        self.rectangle.height = 15
        self.assertEqual(self.rectangle.height, 15)
        self.rectangle.width = 8
        self.assertEqual(self.rectangle.width, 8)

    def test_invalid_setters(self):
        with self.assertRaises(ValueError):
            self.rectangle.y = -1
        with self.assertRaises(ValueError):
            self.rectangle.height = 0
        with self.assertRaises(ValueError):
            self.rectangle.width = -2
        with self.assertRaises(TypeError):
            self.rectangle.y = "invalid"
        with self.assertRaises(TypeError):
            self.rectangle.height = "invalid" 
        with self.assertRaises(TypeError):
            self.rectangle.width = "invalid"
        
    def test_area(self):
        self.assertEqual(self.rectangle.area(), 50) 

    def test_str(self):
        self.assertEqual(str(self.rectangle), "[Rectangle] (1) 2/3 - 5/10")

    def test_display(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            self.rectangle.display()
            expected_output = "\n\n\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n"
            self.assertEqual(captured_output.getvalue(), expected_output)
        finally:
            sys.stdout = sys.__stdout__

    def test_update(self):
        self.rectangle.update(2, 3, 4, 5, 6)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 3)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 5)
        self.assertEqual(self.rectangle.y, 6)
        
        self.rectangle.update(width=7, height=8, x=9, y=10, id=11)
        self.assertEqual(self.rectangle.id, 11)
        self.assertEqual(self.rectangle.width, 7)
        self.assertEqual(self.rectangle.height, 8)
        self.assertEqual(self.rectangle.x, 9)
        self.assertEqual(self.rectangle.y, 10)

    def test_to_dictionary(self):
        dictionary_representation = {
            'id': 1,
            'x': 2,
            'width': 5,
            'height': 10,
            'y': 3
        }
        self.assertEqual(self.rectangle.to_dictionary(), dictionary_representation)

if __name__ == '__main__':
    unittest.main()
