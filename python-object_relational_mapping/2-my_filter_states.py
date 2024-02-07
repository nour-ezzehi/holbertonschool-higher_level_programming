#!/usr/bin/python3
"""list from databases states with a given name"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    connects to a MySQL server and lists all states
        from the database hbtn_0e_0_usa
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

    query = "SELECT * FROM states WHERE BINARY name ='{}'ORDER By id".format(
        name)

    """exeute SQL Query"""
    cur.execute(query)

    """fetch Query results"""
    results = cur.fetchall()

    for result in results:
        print(result)
