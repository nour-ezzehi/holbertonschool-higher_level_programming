#!/usr/bin/python3
"""unittest for base.py"""

import unittest
from models.base import Base
import json
import os
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    
    def tearDown(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_instantiation_with_id_none(self):
        obj = Base()
        self.assertIsInstance(obj, Base)
        self.assertIsNotNone(obj.id)

    def test_instantiation_with_id_provided(self):
        obj = Base(5)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 5)

    def test_incrementing_id_across_instances(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 2)
        self.assertEqual(obj2.id, 3)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_valid_input(self):
        input_data = [{'key': 'value'}, {'another_key': 'another_value'}]
        result = Base.to_json_string(input_data)
        expected_result = json.dumps(input_data)
        self.assertEqual(result, expected_result)

    def test_save_to_file(self):
        rectangle = Rectangle(width=5, height=10, x=2, y=3, id=1)
        square = Square(size=5, x=2, y=3, id=2)
        self.assertFalse(os.path.exists("Rectangle.json"))

        Base.save_to_file([rectangle, square])
        self.assertFalse(os.path.exists("Rectangle.json"))
    
    def test_from_json_string(self):
        json_string = '[{"id": 1, "x": 2, "y": 3, "width": 5, "height": 10}, {"id": 2, "x": 2, "y": 3, "size": 5}]'
        result = Base.from_json_string(json_string)
        expected_result = [{'id': 1, 'x': 2, 'y': 3, 'width': 5, 'height': 10}, {'id': 2, 'x': 2, 'y': 3, 'size': 5}]
        self.assertEqual(result, expected_result)
        empty_json_string = ''
        result_empty = Base.from_json_string(empty_json_string)
        self.assertEqual(result_empty, [])
        result_none = Base.from_json_string(None)
        self.assertEqual(result_none, [])

    def test_create_rectangle(self):
        dictionary = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        result = Rectangle.create(**dictionary)
        self.assertIsInstance(result, Rectangle)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.width, 10)
        self.assertEqual(result.height, 7)
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 8)
    
if __name__ == '__main__':
    unittest.main()
