#!/usr/bin/python3
"""
This module contains one function print_states()
"""

from sys import argv
import MySQLdb


def print_states():
    """
    Print all rows in Table states
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    print_states()
