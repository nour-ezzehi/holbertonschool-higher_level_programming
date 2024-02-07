#!/usr/bin/python3
"""object from json file"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""

    with open(filename, "r") as filename:
        return json.load(filename)
