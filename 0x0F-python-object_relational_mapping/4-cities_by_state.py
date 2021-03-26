#!/usr/bin/env python3
"""
A python script that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
	conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
						   passwd=argv[2], db=argv[3], charset="utf8")
	cur = conn.cursor()
	cur.execute("SELECT * FROM cities ORDER BY id ASC")
	query_rows = cur.fetchall()
	for row in query_rows:
		print(row)
	cur.close()
	conn.close()
