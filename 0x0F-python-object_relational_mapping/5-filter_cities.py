#!/usr/bin/python3
"""
A python script that takes in the name of a state as an argument and
lists all cities of that state
(This script is safe from MySQL injections)
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name LIKE %s ORDER BY cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    print(", ".join(city[0] for city in query_rows))
    cur.close()
    conn.close()
