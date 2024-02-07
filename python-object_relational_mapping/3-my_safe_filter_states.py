#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
 takes in arguments and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument
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

    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id"

    """exeute SQL Query"""
    cur.execute(query, (name,))

    """fetch Query results"""
    results = cur.fetchall()

    for result in results:
        print(result)
