#!/usr/bin/python3
"""lists all cities of that state, using the database hbtn_0e_4_usa"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    takes in the name of a state as an argument and lists all
        cities of that state
    """

    username, password, database, name = sys.argv[1:5]

    """connect to my database"""
    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306)

    """Create a cursor object"""
    cur = db.cursor()

    query = "SELECT cities.name \
            FROM states JOIN cities ON states.id = cities.state_id \
            WHERE states.name = '{}'".format(name)

    """exeute SQL Query"""
    cur.execute(query)

    """fetch Query results"""
    results = cur.fetchall()

    city_names = [result[0] for result in results]
    print(', '.join(city_names))
